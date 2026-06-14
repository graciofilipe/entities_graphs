---
name: bigquery-graph
description: Implements BigQuery Property Graphs. Use when generating BigQuery schemas, writing GQL or SQL graph queries, modeling entities/relationships, or building property graphs in BigQuery.
---

# BigQuery Graph Skill

When working with BigQuery Graph features for this project, you must follow official guidelines and syntax. BigQuery graph uses property graph models and allows you to query them using `GRAPH_TABLE` and graph pattern matching.

## When to use this skill

- Designing schemas for graph node tables and edge tables.
- Writing `CREATE PROPERTY GRAPH` statements.
- Writing queries using the `GRAPH_TABLE` function and graph pattern matching.
- Optimizing and structuring BigQuery graph queries.

## Core Concepts & Best Practices

1. **Node and Edge Tables**: BigQuery graphs are built on top of standard BigQuery tables. You define Node tables (entities like People, Places) and Edge tables (relationships like Visited). 
2. **CREATE PROPERTY GRAPH**: Always use this DDL to define the graph schema. Ensure you specify `KEY` for nodes and `SOURCE KEY` / `DESTINATION KEY` for edges.
3. **Querying with GRAPH_TABLE**: Use `GRAPH_TABLE` combined with `MATCH` to traverse relationships. Example:
   ```sql
   SELECT * FROM GRAPH_TABLE(my_project.my_dataset.my_graph
     MATCH (p:Person)-[v:Visited]->(pl:Place)
     COLUMNS (p.name, pl.name AS place_name)
   )
   ```
4. **Best Practices**:
   - Filter early in your SQL queries before or inside the `GRAPH_TABLE` statement to reduce the data volume.
   - Ensure foreign key references in edge tables map correctly to keys in node tables.
   - Use explicit typing for your graph properties.

## Required Documentation References
Always refer back to these documents when unsure about the syntax or capabilities:
- [Graph Overview](https://docs.cloud.google.com/bigquery/docs/graph-overview)
- [Create Graphs](https://docs.cloud.google.com/bigquery/docs/graph-create)
- [Schema Overview](https://docs.cloud.google.com/bigquery/docs/graph-schema-overview)
- [Query Overview](https://docs.cloud.google.com/bigquery/docs/graph-query-overview)
- [Query Best Practices](https://docs.cloud.google.com/bigquery/docs/graph-query-best-practices)
- [Graph Measures](https://docs.cloud.google.com/bigquery/docs/graph-measures)
- [Graph Modeler](https://docs.cloud.google.com/bigquery/docs/graph-modeler)
- [Graph Visualization](https://docs.cloud.google.com/bigquery/docs/graph-visualization)
- [Graph Chat](https://docs.cloud.google.com/bigquery/docs/graph-chat)
- [Graph Visualization Integrations](https://docs.cloud.google.com/bigquery/docs/graph-visualization-integrations)
- [Graph Search](https://docs.cloud.google.com/bigquery/docs/graph-search)
