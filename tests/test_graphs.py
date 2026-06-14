import pytest
from unittest.mock import MagicMock, patch
from src.bigquery_graph_setup import GraphSetup

@patch('src.bigquery_graph_setup.bigquery.Client')
def test_graph_setup_init(mock_client):
    """Test that the GraphSetup class initializes correctly."""
    setup = GraphSetup(project_id="test-project", dataset_id="test_dataset")
    assert setup.dataset_ref == "test-project.test_dataset"
    mock_client.assert_called_once_with(project="test-project")
    
@patch('src.bigquery_graph_setup.bigquery.Client')
def test_create_node_tables(mock_client):
    """Test node table creation calls."""
    setup = GraphSetup(project_id="test-project", dataset_id="test_dataset")
    setup.client.create_table = MagicMock()
    setup.create_node_tables()
    
    # We should have created exactly two node tables (people and places)
    assert setup.client.create_table.call_count == 2
