---
name: adk-agent-development
description: Use this skill when developing and deploying agents using the Gemini Enterprise Agent Platform and the Agent Development Kit (ADK). Provides the mandatory documentation links for agent creation, runtime setup, and BigQuery integration.
---

# ADK Agent Development Skill

When designing, developing, or deploying agents for the Gemini Enterprise Agent Platform (using ADK), you MUST follow the official documentation. You are required to consult the following URLs to guide your implementation.

Use the `read_url_content` tool on these links to read the documentation when working on agent development tasks.

## Official Portal and Framework Overviews
- [Core ADK Portal](https://adk.dev/)
- [ADK Version 2.0 Feature Overview and Migration Guide](https://adk.dev/2.0/)
- [About the Agent Development Kit](https://adk.dev/get-started/about/)
- [Getting Started Home](https://adk.dev/get-started/)
- [ADK Integrations](https://adk.dev/integrations/)
- [ADK BigQuery Integration](https://adk.dev/integrations/bigquery/)

## Language-Specific Quickstart Guides
- [Python Quickstart Guide](https://adk.dev/get-started/python/)

## API Reference and Command-Line Interface
- [API Reference Landing](https://adk.dev/api-reference/)
- [ADK Python API Reference](https://adk.dev/api-reference/python/)
- [CLI Command Reference](https://adk.dev/api-reference/cli/)

## Runtime and Execution Architecture
- [Ways to Run and Test Agents](https://adk.dev/runtime/)
- [Event Loop, Runner, and Context Guide](https://adk.dev/runtime/event-loop/)
- [RunConfig Schema Parameters](https://adk.dev/runtime/runconfig/)

## Agent Design and Workspace Concepts
- [Structural Concepts and Agent Architecture](https://adk.dev/agents/)
- [AI Model Integration and Routing](https://adk.dev/agents/models/)
- [Workflow Patterns and Sub-Agent Logic](https://adk.dev/agents/workflow-agents/)

## Workflow Design and Collaboration
- [Multi-Agent Workflow Architectures](https://adk.dev/workflows/)
- [Workflow Patterns Reference](https://adk.dev/workflows/patterns/)
- [Collaborative Teams and Coordination Modes](https://adk.dev/workflows/collaboration/)
- [Dynamic Code-Based Workflows](https://adk.dev/graphs/dynamic/)

## Deployment and Infrastructure
- [Google Cloud Agent Platform Agent Runtime Overview](https://adk.dev/deploy/agent-runtime/)

## Evaluation and Performance Optimization
- [Evaluation Framework Overview](https://adk.dev/evaluate/)
- [Evaluation Criteria Metrics](https://adk.dev/evaluate/criteria/)
- [Custom Evaluation Metrics](https://adk.dev/evaluate/custom_metrics/)
- [User Simulation and Scenario Models](https://adk.dev/evaluate/user-sim/)
- [Prompt Optimization via adk optimize](https://adk.dev/optimize/)

## Official GitHub Repositories
- [ADK Documentation Home Repository](https://github.com/google/adk-docs)
- [Python ADK Repository](https://github.com/google/adk-python)

## Core Platform & Concepts
- [Gemini Enterprise Agent Platform Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
- [Conceptual Guide to Agentic Systems](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)
- [Platform Build Framework Options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build)
- [Introduction to the Agent Development Kit (ADK)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk)

## Code-First Agent Development & Quickstarts
- [Quickstart ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/quickstart-adk)
- [Build Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build)
- [Create an Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent)
- [Developing an ADK Agent App](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-adk-agent)
- [Agent Platform Runtime Python SDK Setup](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/quickstart)
- [Interacting with Prebuilt and Custom Sandbox Agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents/interact-with-agents)
- [Cloud Run Quickstart: Automated ADK Deployments](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service)
- [Buildpacks Python Runtime Specification](https://docs.cloud.google.com/docs/buildpacks/python)
- [Google Cloud Buildpacks Reference Documentation](https://docs.cloud.google.com/docs/buildpacks)

## Managed Runtime (Agent Engine) & Deployment
- [Deploy an Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent)
- [Agent Runtime Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime)
- [Setup Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/setup)
- [Querying and Invoking Deployed ADK Agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-adk-agent)
- [Interacting with Deployed Agents via CLI or Console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-agent)
- [Managing and Updating Deployed Runtime Agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents)
- [Troubleshooting Agent Runtime Deployments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment)

## Identity, Governance, and Security
- [Agent Identity Conceptual Architecture](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)
- [Configuring and Authorizing Deployed Runtime Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity)
- [Managing Credentials and Secrets for Deployed Agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-agent-access)
- [Enforcing Agentic Communication Policy Boundaries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview)
- [Agent Gateway Conceptual Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)
- [Set up and Configure an Agent Gateway Resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway)
- [Routing Agent Runtime Egress and Ingress Traffic through Gateways](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-gateway-runtime-deploy)

## Sessions & Memory Bank State Management
- [Managing Session State with the Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-adk)
- [Managing Sessions via Cloud Console or Platform API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-api)
- [Initializing and Configuring Memory Bank Instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup)
- [Integrating ADK Agents with a Managed Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/adk-quickstart)
- [Memory Bank API Quickstart and Payloads](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/api-quickstart)
- [Scope-Level IAM Conditions for Stored Memories](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/iam-conditions)

## Observability, Metrics, and Optimization
- [Introduction to the Platform Optimization Plane](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize)
- [Automating Prompt Tuning using the ADK Optimization CLI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent)
- [Cloud Observability and Metrics Telemetry Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview)
- [Navigating and Interpreting Distributed Agent Traces](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/traces)
- [Visualizing Multi-Agent Architectures with Topology Graphs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/topology)

## Gemini Enterprise App & API Integration
- [Registering and Managing ADK Agents inside the Gemini Enterprise App](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent)
- [REST API Reference: ReasoningEngine Resource Deployment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines)
- [REST API Reference: ReasoningEngineSpec Definitions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ReasoningEngineSpec)

## How to use this skill
1. Before starting an implementation plan for an agent, read the "Get Started" and "Create an Agent" pages to understand the expected framework and project structure.
2. If the agent needs to interact with BigQuery, read the "ADK BigQuery Integration" page for the correct SDK methods and configurations.
3. Incorporate the findings into your implementation approach.
