# Architecture Overview

The Smart Portfolio Performance Analyzer follows a modular, layered design.

## 1. Data Flow

Portfolio Input → Market Data Fetch → Return Engine → Risk Metrics → Reporting Layer

## 2. Modules

### Core
Handles financial computations including:
- Return calculations
- Risk-adjusted performance
- Drawdown analysis

### Data
Responsible for:
- Fetching market prices
- Loading portfolio inputs
- Mapping sectors

### Reporting
Responsible for:
- Visualization
- PDF generation
- Commentary synthesis

## 3. Design Principles

- Separation of concerns
- Testable modules
- Scalable structure
- Minimal external dependencies
