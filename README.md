System Health Check Automation
Why I Built This

While learning more about reliability engineering and automation practices, I started thinking about how many operational checks in enterprise environments are still performed manually.

In many production systems, engineers follow runbooks — step-by-step instructions to verify disk space, memory usage, and service health. These checks are repetitive but critical for stability and compliance.

I wanted to practice converting a simple manual checklist into an automated workflow using Python.

What This Script Does

This script performs basic system health checks:

Evaluates disk usage

Evaluates memory usage

Logs results with timestamps

Flags warnings when usage exceeds a defined threshold

The goal is to simulate how manual operational validation steps can be standardized and automated to reduce human error and improve consistency.

What I Focused On

Clear logging for traceability

Threshold-based alert logic

Simple, readable structure

Reproducible output

This project reflects my interest in automation, system reliability, and building tooling that improves operational efficiency.

Tech Stack

Python

psutil
