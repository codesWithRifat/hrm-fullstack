# Business Requirements Document (BRD)

## 1. Document Information

Project Name: TechQube HRM  
Company: TechQube  
Document Type: Business Requirements Document  
Version: 1.0  
Status: Draft  

---

## 2. Project Overview

TechQube HRM is a web-based Human Resource Management system intended to help organizations manage employee information and common HR operations through a centralized application.

The system will gradually support:

- Employee management
- Departments
- Job positions
- Attendance
- Leave management
- Payroll
- Recruitment
- Reporting
- User roles and permissions

The project will also be used to practice the complete software development lifecycle, including requirements analysis, architecture, development, testing, deployment, and maintenance.

---

## 3. Business Problem

Many small and medium organizations manage HR information using spreadsheets, paper documents, messaging applications, and disconnected systems.

This can create problems such as:

- Duplicate employee information
- Difficulty finding employee records
- Manual attendance tracking
- Manual leave calculations
- Lack of proper approval workflows
- Payroll calculation errors
- Poor visibility of HR data
- Limited reporting
- Lack of access control
- Difficulty maintaining historical records

TechQube HRM aims to provide a centralized system for managing these processes.

---

## 4. Business Objectives

The main business objectives are:

1. Centralize employee information.
2. Reduce manual HR operations.
3. Provide structured employee records.
4. Improve attendance management.
5. Improve leave request and approval workflows.
6. Support payroll processing.
7. Provide role-based access to HR information.
8. Provide useful HR reports and dashboards.
9. Maintain historical HR data.
10. Provide a scalable foundation for future HR functionality.

---

## 5. Stakeholders

### Primary Stakeholders

- Organization Management
- HR Managers
- HR Officers
- Employees
- Department Managers

### Secondary Stakeholders

- Payroll Officers
- System Administrators
- Recruitment Officers
- Developers
- Auditors

---

## 6. User Roles

### Administrator

Responsible for:

- System configuration
- User management
- Roles and permissions
- Global access

### HR Manager

Responsible for:

- Employee management
- Department management
- Attendance review
- Leave approval
- Payroll management
- HR reporting

### Department Manager

Responsible for:

- Viewing department employees
- Reviewing employee attendance
- Reviewing or approving leave where applicable

### Employee

Responsible for:

- Viewing own profile
- Viewing attendance
- Applying for leave
- Viewing leave balances
- Viewing payslips

---

## 7. Business Scope

### In Scope

The planned system will include:

- Multi-company management
- Authentication
- User management
- Employee management
- Department management
- Job positions
- Attendance
- Leave management
- Multi-level approvals
- Configurable payroll rules
- Payroll processing
- Recruitment
- Dashboard and analytics
- HR reports
- PDF reporting
- Search, filtering, and grouping
- Role-based access control
- Auditability

### Out of Scope for Initial Releases

The following are not part of the initial development scope:

- Full accounting
- Inventory
- Sales
- CRM
- Manufacturing
- Advanced biometric device integration
- Government tax filing integrations
- Mobile applications

These may be considered in future versions.

---

## 8. High-Level Business Requirements

| ID | Requirement | Business Requirement |
|---|---|---|
| BR-001 | Multi-Company Management | The system must support multiple companies within a single installation. Company-specific employees, departments, job positions, attendance, leave, payroll, recruitment, reports, and configuration must remain logically separated. |
| BR-002 | Employee Management | The system must allow authorized users to create, view, update, archive, search, and filter employee records. |
| BR-003 | Department Management | The system must allow organizations to define departments and assign employees and department managers to them. |
| BR-004 | Job Position Management | The system must allow job positions to be created, updated, archived, and assigned to employees. |
| BR-005 | Attendance Management | The system must allow employee check-in/check-out records to be created, reviewed, corrected by authorized users, and used for attendance reporting. |
| BR-006 | Leave Management | The system must allow employees to request leave, view leave balances, and track request status. Leave types and allocation rules must be configurable. |
| BR-007 | Multi-Level Approval Workflow | Leave and other applicable HR requests must support approval workflows. The default leave approval flow will be Employee → Line Manager → HR Manager → Approved. |
| BR-008 | Configurable Payroll Rules | The system must support configurable payroll rules so authorized users can create salary components such as basic salary, allowances, deductions, bonuses, overtime, tax, and other custom rules without modifying application source code. |
| BR-009 | Payroll Processing | The system must support payroll calculation, salary structures, payroll periods, employee payslips, payroll finalization, and payroll history. |
| BR-010 | Recruitment | The system should support job vacancies, candidates, applications, recruitment stages, interviews, and hiring status. |
| BR-011 | User Access & Security | The system must restrict access to functionality and data according to user roles, permissions, company access, and employee relationships. |
| BR-012 | Dashboard & Analytics | The system must provide dashboards containing useful HR indicators and summary information based on the user's role and company access. |
| BR-013 | Reports | The system must provide standard HR reports for employees, attendance, leave, payroll, recruitment, and organizational information. |
| BR-014 | PDF Reports | Users with appropriate permissions must be able to generate and download selected business reports and documents in PDF format. |
| BR-015 | Auditability | Important HR records and business transactions must retain sufficient historical and audit information for review. |
| BR-016 | Search & Filtering | Major HR records must support practical searching, filtering, sorting, and grouping to help users find information efficiently. |


### 8.1 Minimum Reporting Requirements

The first production-capable version of TechQube HRM should provide a basic set of operational reports.

#### Employee Reports

- Employee List
- Active Employees
- Archived / Former Employees
- Employees by Department
- Employees by Job Position
- Employees by Company
- New Joiners
- Employee Headcount Summary

#### Attendance Reports

- Daily Attendance
- Monthly Attendance
- Employee Attendance History
- Late Attendance
- Missing Check-Out
- Absent Employees
- Working Hours Summary

#### Leave Reports

- Leave Requests
- Approved Leave
- Pending Leave
- Rejected Leave
- Employee Leave Balance
- Leave Usage by Type
- Leave Summary by Department

#### Payroll Reports

- Payroll Summary
- Employee Payroll Details
- Payslip
- Salary Component Summary
- Allowance Summary
- Deduction Summary
- Payroll by Department
- Payroll by Company

#### Recruitment Reports

- Open Vacancies
- Candidate Applications
- Candidates by Recruitment Stage
- Hiring Summary

#### Organization Reports

- Department List
- Job Position List
- Department Headcount
- Company Headcount

### 8.2 Dashboard Requirements

The system should provide role-based dashboards containing key HR information.

#### HR Dashboard

The HR dashboard should initially include:

- Total Employees
- Active Employees
- New Joiners
- Employees by Department
- Employees by Company
- Employees Present Today
- Employees Absent Today
- Employees on Leave Today
- Pending Leave Requests
- Upcoming Employee Birthdays
- Open Job Vacancies
- Recent HR Activities

#### Manager Dashboard

A line manager should be able to view information relevant to employees under their responsibility, including:

- Team Headcount
- Team Attendance Today
- Team Members on Leave
- Pending Leave Approvals
- Recent Leave Requests

#### Employee Dashboard

An employee should be able to view personal information such as:

- Attendance Status
- Recent Attendance
- Leave Balance
- Pending Leave Requests
- Latest Payslip
- Basic Employee Profile Information

### 8.3 PDF Reporting Requirements

Selected reports and HR documents must support PDF generation.

Initial PDF outputs should include:

- Employee Profile
- Employee List
- Attendance Report
- Leave Report
- Leave Request / Approval Record
- Payslip
- Payroll Summary
- Department Employee Report

PDF documents should contain, where applicable:

- Company name
- Company logo
- Report title
- Reporting period
- Generation date
- User who generated the report
- Page number
- Structured tabular information
---

## 9. Business Rules

1. Each employee must have a unique employee identifier within the applicable company.
2. Employee and HR records must belong to a company where applicable.
3. Users may be granted access to one or multiple companies.
4. An employee may belong to one primary department at a time.
5. An employee may have one active primary job position at a time.
6. Leave types may have different allocation, eligibility, and validation rules.
7. The default leave approval workflow is Line Manager approval followed by HR Manager approval.
8. If an employee does not have an assigned line manager, the workflow may route directly to the HR Manager according to configuration.
9. A leave request must complete the required approval process before being considered approved.
10. Payroll salary components must be defined through configurable payroll rules.
11. Payroll rules may represent earnings, allowances, deductions, employer contributions, or other configurable salary components.
12. Finalized payroll records must not be silently altered.
13. Changes to finalized payroll should require an explicit correction or controlled reopening process.
14. Users must only access functionality and company data permitted by their roles and permissions.
15. Archived employees must remain available for historical reporting.
16. Sensitive employee and payroll information must not be accessible to unauthorized users.
17. Reports must respect the same company and security access rules as normal application records.
18. PDF reports must only include information the requesting user is authorized to access.

---

## 10. Assumptions

- Organizations using the system have internet or local network access.
- Users have modern web browsers.
- HR users are responsible for maintaining accurate employee information.
- PostgreSQL will be available as the application database.
- The application will initially be browser-based.

---

## 11. Constraints

- The project is being developed incrementally.
- Initial infrastructure resources may be limited.
- The application must remain maintainable by a small development team.
- The architecture should avoid unnecessary complexity.
- Development will use open-source technologies where practical.

---

## 12. Success Criteria

The project will be considered successful when:

- Authorized users can manage employees through the web interface.
- Employee data is stored reliably in PostgreSQL.
- Authentication and permissions are enforced.
- Core HR workflows function correctly.
- Frontend and backend communicate through REST APIs.
- Automated tests cover important functionality.
- The application can be deployed using Docker.
- The project documentation accurately reflects the implemented system.

---

## 13. Risks

Potential project risks include:

- Scope becoming too large.
- Overengineering early architecture.
- Incomplete requirements.
- Insufficient testing.
- Security mistakes.
- Poor database design.
- Inconsistent frontend and backend contracts.
- Learning multiple technologies simultaneously.

These risks will be controlled through incremental development and Agile-style sprints.

---

## 14. Future Opportunities

Possible future enhancements include:

- Mobile application
- Biometric attendance integration
- GPS-based mobile attendance
- RFID / card attendance integration
- Advanced employee self-service
- Expense management
- Performance appraisal
- Training management
- Document management
- Advanced workflow configuration
- Multi-language support
- Advanced HR analytics
- AI-assisted HR analytics
- Employee onboarding workflows
- Employee offboarding workflows
- Advanced benefits management
- Cloud SaaS deployment

---

## 15. Approval Status

Current Status: Draft

This BRD will evolve as project requirements become clearer.
