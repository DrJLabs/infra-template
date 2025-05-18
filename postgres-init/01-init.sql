-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";
CREATE EXTENSION IF NOT EXISTS "btree_gin";
CREATE EXTENSION IF NOT EXISTS "btree_gist";

-- Optimize for n8n workflow storage
ALTER SYSTEM SET synchronous_commit = 'off';

-- Create optimized indexes for n8n tables (will be created after n8n initializes)
CREATE OR REPLACE FUNCTION create_n8n_indexes() 
RETURNS void AS $$
BEGIN
    -- Wait for tables to be created by n8n
    PERFORM pg_sleep(30);
    
    -- Create indexes if tables exist
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'execution_entity') THEN
        -- Optimize execution entities lookup
        CREATE INDEX IF NOT EXISTS idx_execution_entity_workflow_id ON execution_entity(workflowId);
        CREATE INDEX IF NOT EXISTS idx_execution_entity_status ON execution_entity(status);
        CREATE INDEX IF NOT EXISTS idx_execution_entity_finished_at ON execution_entity(finished);
        
        -- Optimize for time-based queries
        CREATE INDEX IF NOT EXISTS idx_execution_entity_started_at ON execution_entity(startedAt);
        CREATE INDEX IF NOT EXISTS idx_execution_entity_waited_at ON execution_entity(waitTill);
        
        -- Optimize for combined status and date filters
        CREATE INDEX IF NOT EXISTS idx_execution_entity_status_started_at ON execution_entity(status, startedAt);
    END IF;

    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'workflow_entity') THEN
        -- Optimize workflow lookup
        CREATE INDEX IF NOT EXISTS idx_workflow_entity_active ON workflow_entity(active);
        CREATE INDEX IF NOT EXISTS idx_workflow_entity_name ON workflow_entity(name);
    END IF;

    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'workflow_statistics') THEN
        -- Optimize statistics lookup
        CREATE INDEX IF NOT EXISTS idx_workflow_statistics_workflow_id ON workflow_statistics(workflowId);
        CREATE INDEX IF NOT EXISTS idx_workflow_statistics_day ON workflow_statistics(day);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Set up autovacuum for n8n tables
ALTER SYSTEM SET autovacuum_vacuum_scale_factor = 0.05;
ALTER SYSTEM SET autovacuum_analyze_scale_factor = 0.025;
ALTER SYSTEM SET autovacuum_vacuum_threshold = 50;
ALTER SYSTEM SET autovacuum_analyze_threshold = 50;

-- Plan function execution after database startup
CREATE OR REPLACE FUNCTION execute_after_startup() RETURNS void AS $$
BEGIN
    PERFORM pg_notify('db_startup', 'execute_indexing');
END;
$$ LANGUAGE plpgsql;

-- Event trigger setup - disabled due to compatibility issue
-- 'startup' is not a valid event type in PostgreSQL 15
-- CREATE EVENT TRIGGER startup_trigger
-- ON startup
-- EXECUTE PROCEDURE execute_after_startup(); 