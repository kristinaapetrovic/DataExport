# PDF Exporter for Route Data

This Python project generates PDF reports from structured route data. It uses the `ReportLab` library to create a landscape-oriented PDF 
containing a table of duct and accessory parameters.

## Features

- Converts route data stored in Python dictionaries into a PDF table.
- Supports long tables with headers and grid lines.
- Aligns textual and numerical columns for better readability.
- Simple and lightweight solution without external databases.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
pip install reportlab

| Column      | Description                                         |
| ----------- | --------------------------------------------------- |
| Node        | Node identifier                                     |
| Level       | Level of the system                                 |
| Type        | Type of component (Duct, Accessory, Terminal, etc.) |
| Product     | Product name                                        |
| Size        | Dimensions                                          |
| L [m]       | Length                                              |
| Flow [m³/h] | Airflow                                             |
| v [m/s]     | Velocity                                            |
| dtp [Pa]    | Pressure drop                                       |
| K factor    | K factor                                            |
| Δp/L        | Pressure drop per length                            |
| pt          | Total pressure                                      |
| pst         | Static pressure                                     |
| adj.        | Adjustment                                          |
| Warnings    | Any warnings                                        |

