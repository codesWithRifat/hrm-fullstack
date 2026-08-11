# TechQube HRM
# Functional Requirements Document (FRD)

## Document Information

| Field | Value |
|---|---|
| Project Name | TechQube HRM |
| Company | TechQube |
| Document Type | Functional Requirements Document |
| Version | 1.0 |
| Status | Draft |
| Application Type | Web-Based HRM |
| Related BRD | BRD v1.0 |
| Related Document | User Story Catalog |

---

# 1. Purpose

This Functional Requirements Document defines the expected functional behavior of the TechQube HRM application.

The document translates the approved business requirements and user stories into detailed functional requirements that will guide:

- Frontend development
- Backend API development
- Database design
- Authentication and authorization
- Workflow implementation
- Reporting
- Testing
- Acceptance criteria

The document focuses primarily on **what the system must do**.

Technical architecture, detailed database design, infrastructure design, and low-level API specifications will be documented separately.

---

# 2. System Overview

TechQube HRM will be a browser-based Human Resource Management platform.

Users will interact with the application through a modern web interface.

The application will use the following high-level architecture:

```text
Web Browser
    │
    ▼
React + TypeScript Frontend
    │
    │ REST / JSON
    ▼
FastAPI Backend
    │
    │ SQLAlchemy
    ▼
PostgreSQL Database
```

The system will initially support desktop and modern browser usage while maintaining a responsive design suitable for tablets and smaller screens where practical.

---

# 3. Functional Scope

The application will contain the following major functional areas:

1. Multi-Company Management
2. Authentication
3. Users, Roles and Permissions
4. Employee Management
5. Employee Self-Service
6. Organization Structure
7. Manager Self-Service
8. Attendance
9. Leave Management
10. Approval Workflows
11. Payroll
12. Recruitment
13. Dashboard
14. Reports
15. PDF Reports
16. Search and Filtering
17. Audit and Data Integrity

---

# 4. User Interface Requirements

## FR-UI-001 — Web Application

The system shall be accessible through a modern web browser.

Supported application behavior shall include:

- Navigation without requiring full page reloads where practical
- Responsive page layouts
- Forms
- Tables
- Search
- Filters
- Pagination
- Dialogs/modals where appropriate
- Notifications
- Validation messages
- Loading indicators
- Error states

---

## FR-UI-002 — Application Layout

Authenticated users shall be presented with an application layout containing, where appropriate:

- Application logo
- Navigation sidebar
- Top navigation/header
- Active company selector
- User profile menu
- Notifications or pending action indicator
- Main content area

---

## FR-UI-003 — Responsive Design

The interface shall adapt to different screen sizes.

Primary development priority:

1. Desktop
2. Laptop
3. Tablet
4. Mobile browser

A dedicated mobile application is not part of the initial scope.

---

## FR-UI-004 — User Feedback

The frontend shall provide clear feedback for user actions.

Examples:

- Record created successfully
- Record updated successfully
- Request submitted
- Leave approved
- Validation failed
- Unauthorized action
- Network/API error
- Record not found

---

# 5. Multi-Company Management

## FR-COMP-001 — Company Records

Authorized administrators shall be able to create and maintain company records.

Company information may include:

- Company name
- Company code
- Logo
- Address
- Phone
- Email
- Website
- Currency
- Time zone
- Status

---

## FR-COMP-002 — User Company Access

Users shall be assigned access to one or more companies.

The system shall ensure that:

- Users cannot access unauthorized company data.
- Backend authorization enforces company restrictions.
- Frontend menus and selections only show permitted companies.

---

## FR-COMP-003 — Active Company

A user with access to multiple companies shall be able to select an active company.

The active company shall be clearly visible in the interface.

New company-dependent records shall default to the active company.

---

## FR-COMP-004 — Company Data Separation

Company-dependent records shall be associated with a company.

Examples include:

- Employees
- Departments
- Job positions
- Attendance
- Leave
- Payroll
- Recruitment
- Reports

Cross-company access must only occur when explicitly permitted.

---

# 6. Authentication

## FR-AUTH-001 — Login

The system shall provide a login page.

The user shall provide:

- Username/email
- Password

The backend shall verify credentials.

On successful authentication:

- The user shall receive an authenticated session/token.
- The user shall be redirected to the application.

---

## FR-AUTH-002 — Invalid Login

If login fails:

- The user shall remain unauthenticated.
- A generic error message shall be displayed.
- Sensitive authentication details shall not be exposed.

---

## FR-AUTH-003 — Logout

Authenticated users shall be able to log out.

After logout:

- Protected pages shall no longer be accessible.
- Authentication credentials/tokens shall be cleared or invalidated as applicable.

---

## FR-AUTH-004 — Protected Routes

Application pages and API routes requiring authentication shall reject unauthenticated access.

---

# 7. User and Role Management

## FR-USER-001 — User Management

Administrators shall be able to:

- Create users
- View users
- Update users
- Activate users
- Deactivate users
- Assign allowed companies
- Assign roles

---

## FR-USER-002 — Roles

The system shall support application roles such as:

- Administrator
- HR Manager
- HR Officer
- Payroll Manager
- Recruitment Officer
- Line Manager
- Employee

Additional roles may be introduced later.

---

## FR-USER-003 — Permission Enforcement

Permissions shall be enforced at the backend/API level.

Frontend visibility alone shall not be considered sufficient authorization.

---

# 8. Employee Management

## FR-EMP-001 — Employee Creation

Authorized HR users shall be able to create employees through a web form.

Initial employee information may include:

### Identity

- Employee ID
- First name
- Middle name
- Last name
- Display name
- Gender
- Date of birth
- Photograph

### Contact

- Work email
- Personal email
- Work phone
- Personal phone
- Address

### Employment

- Company
- Department
- Job position
- Line manager
- Joining date
- Employment status

### Additional Information

- Emergency contact
- Notes

The exact field model will be finalized during database design.

---

## FR-EMP-002 — Employee Validation

The system shall validate employee data before saving.

Examples:

- Required fields cannot be empty.
- Employee ID must be unique within the applicable company.
- Email format must be valid when provided.
- Referenced company must be accessible to the current user.
- Department and job position must belong to valid organizational structures.

---

## FR-EMP-003 — Employee List

Authorized users shall be able to view employees in a tabular interface.

The list shall support:

- Pagination
- Search
- Sorting
- Filtering

Initial columns may include:

- Employee ID
- Name
- Company
- Department
- Job position
- Manager
- Joining date
- Status

---

## FR-EMP-004 — Employee Profile

Authorized users shall be able to open an employee profile.

The employee profile may be divided into sections such as:

- General Information
- Employment Information
- Contact Information
- Attendance
- Leave
- Payroll
- Documents
- History

Access to sections shall depend on permissions.

---

## FR-EMP-005 — Employee Update

Authorized users shall be able to update employee information.

Changes shall be validated before saving.

---

## FR-EMP-006 — Employee Archive

Employees shall normally be archived rather than permanently deleted.

Archived employees:

- Shall remain in the database.
- Shall not appear in active employee lists by default.
- Shall remain available for historical reporting.
- Shall retain related attendance, leave, and payroll history.

---

# 9. Organization Structure

## FR-ORG-001 — Department Management

Authorized HR users shall be able to:

- Create departments
- View departments
- Update departments
- Archive departments
- Assign department managers

Department records shall belong to a company.

---

## FR-ORG-002 — Job Position Management

Authorized HR users shall be able to:

- Create job positions
- View job positions
- Update job positions
- Archive job positions

Job positions shall belong to a company.

---

## FR-ORG-003 — Line Manager

An employee may have an assigned line manager.

The line-manager relationship shall be used by:

- Manager self-service
- Leave approval
- Team reporting
- Dashboard information

---

# 10. Employee Self-Service

## FR-ESS-001 — My Profile

Employees shall be able to view their own employee profile.

Employees shall not automatically receive permission to view sensitive information belonging to other employees.

---

## FR-ESS-002 — My Attendance

Employees shall be able to view their own attendance records.

The screen should support:

- Date range selection
- Check-in
- Check-out
- Working hours
- Attendance status

---

## FR-ESS-003 — My Leave

Employees shall be able to:

- View leave balances
- Submit leave requests
- View leave request history
- View approval status

---

## FR-ESS-004 — My Payslips

Employees shall be able to view authorized finalized payslips.

---

## FR-ESS-005 — Download Payslip

Employees shall be able to download available payslips in PDF format.

---

# 11. Manager Self-Service

## FR-MGR-001 — My Team

Line managers shall be able to view employees who report to them.

The system shall derive team membership from the employee-manager relationship.

---

## FR-MGR-002 — Team Attendance

Managers with appropriate permissions shall be able to review attendance for employees reporting to them.

---

## FR-MGR-003 — Team Leave

Managers shall be able to review leave information relevant to their team.

---

## FR-MGR-004 — Pending Approvals

Managers shall have access to requests awaiting their approval.

---

# 12. Attendance Management

## FR-ATT-001 — Web Check-In

Authenticated employees shall be able to check in through the web application.

The system shall record:

- Employee
- Company
- Check-in timestamp
- Attendance source

Initial source:

```text
WEB
```

---

## FR-ATT-002 — Prevent Duplicate Check-In

The system shall prevent an employee from creating another active check-in while an unclosed attendance record already exists.

---

## FR-ATT-003 — Web Check-Out

An employee with an active attendance record shall be able to check out.

The system shall record:

- Check-out timestamp
- Calculated duration

---

## FR-ATT-004 — Manual Attendance

Authorized HR users shall be able to create attendance records manually.

The attendance record shall identify its source.

Example sources:

```text
WEB
MANUAL
IMPORT
```

Future sources may include:

```text
BIOMETRIC
MOBILE
API
```

---

## FR-ATT-005 — Attendance Correction

Authorized HR users shall be able to correct attendance records.

Changes shall be auditable where required.

---

## FR-ATT-006 — Working Hours

The system shall calculate worked duration using valid check-in and check-out times.

---

## FR-ATT-007 — Missing Check-Out

The system shall identify attendance records that contain a check-in but no check-out.

Such records shall be visible to authorized HR users for correction.

---

## FR-ATT-008 — Overtime

The system should calculate or identify overtime based on configurable working-time rules.

Detailed overtime policies will be refined later.

---

# 13. Leave Management

## FR-LEV-001 — Leave Types

Authorized HR users shall be able to configure leave types.

Examples:

- Annual Leave
- Casual Leave
- Sick Leave
- Maternity Leave
- Unpaid Leave

A leave type may contain:

- Name
- Code
- Company
- Paid/unpaid indicator
- Approval requirement
- Active status

---

## FR-LEV-002 — Leave Allocation

The system shall support leave entitlements or allocations.

Leave allocation may vary by:

- Company
- Leave type
- Employee
- Employment policy

Detailed accrual rules will be refined later.

---

## FR-LEV-003 — Leave Balance

The system shall calculate and display available leave balance where applicable.

---

## FR-LEV-004 — Submit Leave Request

Employees shall be able to submit a leave request.

Required information shall include:

- Leave type
- Start date
- End date

Optional information may include:

- Reason
- Attachment

---

## FR-LEV-005 — Leave Validation

The system shall validate requests against applicable business rules.

Examples:

- Start date cannot be after end date.
- Leave type must be active.
- Employee must be eligible.
- Available balance must be sufficient where balance control applies.
- Invalid overlapping requests should be prevented.

---

# 14. Leave Approval Workflow

## FR-APR-001 — Initial State

A newly created leave request shall begin in an editable/draft or submitted state depending on the interface design.

---

## FR-APR-002 — Submit for Approval

When an employee submits a request, the workflow shall determine the required approver.

Default process:

```text
Employee
    │
    ▼
Line Manager
    │
    ▼
HR Manager
    │
    ▼
Approved
```

---

## FR-APR-003 — Line Manager Approval

The line manager shall be able to:

- View the request
- Approve
- Reject

If approved:

```text
Awaiting HR Approval
```

If rejected:

```text
Rejected
```

---

## FR-APR-004 — HR Approval

The HR Manager shall provide final approval.

Possible actions:

- Approve
- Reject

---

## FR-APR-005 — Missing Line Manager

If an employee does not have a line manager, the system shall allow the configured workflow to route the request directly to an HR Manager.

---

## FR-APR-006 — Approval History

The system shall retain approval history including where appropriate:

- Approver
- Action
- Timestamp
- Comment/reason

---

## FR-APR-007 — Rejection Reason

A rejection shall require or support a rejection reason according to workflow configuration.

For the initial version, rejection reason should be mandatory.

---

# 15. Payroll Configuration

## FR-PAY-001 — Payroll Rule

Authorized payroll users shall be able to create payroll rules without modifying application source code.

---

## FR-PAY-002 — Payroll Rule Information

A payroll rule may contain:

- Name
- Code
- Company
- Category
- Sequence
- Calculation method
- Calculation base
- Amount
- Percentage
- Condition
- Active status

---

## FR-PAY-003 — Payroll Rule Categories

Initial payroll categories may include:

- Basic
- Allowance
- Deduction
- Bonus
- Overtime
- Employer Contribution
- Tax
- Net

The structure should allow additional categories if required.

---

## FR-PAY-004 — Calculation Methods

Initial supported calculation methods should include:

### Fixed Amount

Example:

```text
Medical Allowance = 2,000
```

### Percentage

Example:

```text
House Rent = 50% of Basic Salary
```

Additional calculation methods may be introduced during detailed payroll design.

---

## FR-PAY-005 — Salary Structure

Authorized payroll users shall be able to create salary structures.

A salary structure shall group payroll rules.

Example:

```text
Monthly Employee Salary Structure

Basic Salary
House Rent
Medical Allowance
Overtime
Tax
Provident Fund
Net Salary
```

---

## FR-PAY-006 — Employee Payroll Configuration

Employees participating in payroll shall have applicable compensation configuration.

The exact design may involve:

- Contract
- Salary structure assignment
- Base salary
- Effective dates

This will be finalized during payroll data-model design.

---

# 16. Payroll Processing

## FR-PRC-001 — Payroll Period

Payroll processing shall operate for a defined payroll period.

Initial implementation is expected to prioritize monthly payroll.

The architecture should avoid unnecessarily preventing future support for alternative pay periods.

---

## FR-PRC-002 — Payroll Batch

Authorized payroll users shall be able to initiate payroll processing for:

- Company
- Payroll period
- Eligible employees

---

## FR-PRC-003 — Calculate Payroll

The system shall calculate payroll according to:

- Employee salary configuration
- Salary structure
- Payroll rules
- Applicable attendance/worked-time information
- Applicable leave information
- Manual payroll inputs where supported

---

## FR-PRC-004 — Payroll Review

Before finalization, payroll users shall be able to review:

- Earnings
- Allowances
- Deductions
- Gross salary
- Net salary
- Rule-level calculation details

---

## FR-PRC-005 — Payroll Finalization

Authorized users shall be able to finalize reviewed payroll.

Finalized payroll must be protected from silent modification.

---

## FR-PRC-006 — Payroll Reopening

If correction of finalized payroll is required, the action must be explicit and permission-controlled.

The system shall not silently edit finalized payroll.

---

## FR-PRC-007 — Payslip

The system shall generate a payslip for each processed employee.

A payslip shall display applicable components such as:

- Employee
- Company
- Payroll period
- Basic salary
- Allowances
- Earnings
- Deductions
- Gross salary
- Net salary

---

# 17. Recruitment

## FR-REC-001 — Vacancy

Authorized recruitment users shall be able to create job vacancies.

---

## FR-REC-002 — Candidate

Authorized users shall be able to create and maintain candidate records.

Candidate data may include:

- Name
- Email
- Phone
- Vacancy
- CV/resume
- Notes
- Current stage

---

## FR-REC-003 — Recruitment Stages

Applicants shall move through configurable recruitment stages.

Initial stages may include:

```text
New
Screening
Interview
Offer
Hired
Rejected
```

---

## FR-REC-004 — Interview

Recruitment users shall be able to record interview information.

---

## FR-REC-005 — Hire Candidate

Authorized HR users shall be able to convert or use successful candidate information to create an employee.

---

# 18. Dashboard

## FR-DASH-001 — HR Dashboard

The HR dashboard shall initially provide relevant indicators such as:

- Total employees
- Active employees
- New joiners
- Employees by company
- Employees by department
- Present today
- Absent today
- Employees on leave today
- Pending leave approvals
- Upcoming birthdays
- Open vacancies

---

## FR-DASH-002 — Dashboard Visualization

Dashboard information may be presented using:

- KPI cards
- Tables
- Charts
- Lists

Charts should be interactive where practical.

---

## FR-DASH-003 — Dashboard Filtering

Where relevant, dashboards should support filtering by:

- Company
- Date period
- Department

---

## FR-DASH-004 — Manager Dashboard

Line managers should receive team-relevant information such as:

- Team headcount
- Present today
- Absent today
- Employees on leave
- Pending approvals

---

## FR-DASH-005 — Employee Dashboard

Employees should receive personal information such as:

- Today's attendance status
- Leave balance
- Pending leave requests
- Recent attendance
- Latest payslip

---

# 19. Reports

## FR-RPT-001 — Employee Reports

Initial employee reports shall include:

- Employee List
- Active Employees
- Archived Employees
- Employees by Company
- Employees by Department
- Employees by Job Position
- New Joiners
- Headcount Summary

---

## FR-RPT-002 — Attendance Reports

Initial attendance reports shall include:

- Daily Attendance
- Monthly Attendance
- Employee Attendance History
- Late Attendance
- Missing Check-Out
- Absent Employees
- Working Hours Summary

---

## FR-RPT-003 — Leave Reports

Initial leave reports shall include:

- Leave Requests
- Approved Leave
- Pending Leave
- Rejected Leave
- Leave Balance
- Leave Usage by Type
- Leave by Department

---

## FR-RPT-004 — Payroll Reports

Initial payroll reports shall include:

- Payroll Summary
- Employee Payroll Details
- Payslip
- Salary Component Summary
- Allowance Summary
- Deduction Summary
- Payroll by Department
- Payroll by Company

---

## FR-RPT-005 — Recruitment Reports

Initial recruitment reports should include:

- Open Vacancies
- Candidate Applications
- Candidates by Stage
- Hiring Summary

---

## FR-RPT-006 — Report Filters

Applicable reports shall support filters such as:

- Company
- Department
- Employee
- Date range
- Status
- Payroll period

---

# 20. PDF Reporting

## FR-PDF-001 — PDF Generation

Authorized users shall be able to generate selected reports as PDF documents.

---

## FR-PDF-002 — Initial PDF Documents

Initial PDF support shall include:

- Employee Profile
- Employee List
- Attendance Report
- Leave Report
- Leave Approval Record
- Payslip
- Payroll Summary
- Department Employee Report

---

## FR-PDF-003 — PDF Header

PDF documents shall contain where applicable:

- Company logo
- Company name
- Report title
- Reporting period/date
- Generation date

---

## FR-PDF-004 — PDF Footer

PDF documents should contain:

- Page number
- Generation metadata where appropriate

---

## FR-PDF-005 — PDF Authorization

The PDF generation endpoint shall enforce the same authorization rules as the underlying data.

Generating a PDF shall never bypass normal access restrictions.

---

# 21. Search, Filtering and Pagination

## FR-SRCH-001 — Search

Major list views shall support relevant search capability.

Examples:

- Employees
- Departments
- Leave requests
- Attendance
- Candidates

---

## FR-SRCH-002 — Filtering

Major records shall support context-appropriate filters.

---

## FR-SRCH-003 — Sorting

Table columns should support sorting where practical.

---

## FR-SRCH-004 — Pagination

Large datasets shall be paginated.

Pagination shall primarily be handled by backend APIs rather than loading all records into the browser.

---

# 22. Notifications and Pending Actions

## FR-NOT-001 — Approval Notification

Users responsible for approvals should be informed when a request requires their action.

The initial implementation may use in-application notifications.

Email notifications may be introduced later.

---

## FR-NOT-002 — Employee Status Notification

Employees shall be able to see updates to submitted requests.

Examples:

- Leave awaiting manager approval
- Leave awaiting HR approval
- Leave approved
- Leave rejected

---

# 23. Audit Trail

## FR-AUD-001 — Audit Information

Important business records should retain basic audit metadata such as:

- Created by
- Created at
- Updated by
- Updated at

---

## FR-AUD-002 — Workflow History

Approval-related records shall retain workflow history.

---

## FR-AUD-003 — Payroll History

Finalized payroll information shall remain historically traceable.

---

# 24. API Functional Requirements

The web frontend shall communicate with the backend through REST APIs.

Initial API convention:

```text
/api/v1/
```

Example resources:

```text
/api/v1/auth
/api/v1/companies
/api/v1/users
/api/v1/employees
/api/v1/departments
/api/v1/job-positions
/api/v1/attendance
/api/v1/leave-types
/api/v1/leave-requests
/api/v1/payroll
/api/v1/recruitment
/api/v1/reports
```

Exact endpoints and payloads shall be documented in `API.md`.

---

# 25. Frontend Functional Architecture

The React application should be organized around feature areas.

A possible future structure is:

```text
frontend/src/
│
├── components/
├── layouts/
├── pages/
├── features/
│   ├── auth/
│   ├── companies/
│   ├── employees/
│   ├── organization/
│   ├── attendance/
│   ├── leave/
│   ├── payroll/
│   ├── recruitment/
│   └── reports/
│
├── services/
├── hooks/
├── types/
└── utils/
```

This structure is preliminary and may change during architecture design.

---

# 26. Backend Functional Architecture

The FastAPI backend shall separate responsibilities.

Planned areas include:

```text
backend/app/
│
├── models/
├── schemas/
├── routers/
├── services/
├── core/
├── database.py
└── main.py
```

Responsibilities:

| Layer | Responsibility |
|---|---|
| Routers | HTTP/API handling |
| Schemas | Request/response validation |
| Services | Business logic |
| Models | Database representation |
| Database | PostgreSQL connection/session |
| Core | Shared configuration/security |

Detailed architecture will be defined separately.

---

# 27. Validation Requirements

Validation shall exist at multiple levels.

## Frontend Validation

React forms should provide immediate usability feedback.

Examples:

- Required fields
- Invalid email
- Invalid date range

Frontend validation shall not replace backend validation.

## Backend Validation

FastAPI/Pydantic shall validate incoming request data.

Business rules shall also be validated in backend logic.

## Database Constraints

PostgreSQL shall enforce critical integrity rules where appropriate.

Examples:

- Primary keys
- Unique constraints
- Foreign keys
- Required relationships

---

# 28. Error Handling

The backend shall return structured errors.

Example conceptual response:

```json
{
  "detail": "Employee not found"
}
```

Validation errors should identify invalid fields where practical.

The frontend shall convert backend errors into understandable user feedback.

---

# 29. Security Functional Requirements

The system shall include:

- Authentication
- Authorization
- Company access controls
- Role-based permissions
- Protected API endpoints
- Password hashing
- Secure handling of tokens
- Input validation
- Restricted payroll information
- Restricted employee-sensitive information

Detailed security requirements will be documented in the SRS and Security documentation.

---

# 30. Data Export

Selected reports should support future export formats such as:

- PDF
- CSV

PDF is part of the planned initial reporting functionality.

CSV export may be introduced progressively where useful.

---

# 31. Functional Dependencies

Some modules depend on other modules.

```text
Company
   │
   ├── Department
   │      │
   │      └── Employee
   │
   ├── Job Position
   │      │
   │      └── Employee
   │
   └── Employee
          │
          ├── Attendance
          ├── Leave
          ├── Payroll
          └── Manager Relationship
```

Payroll may depend on:

```text
Employee
   +
Salary Structure
   +
Payroll Rules
   +
Attendance
   +
Leave
   +
Payroll Inputs
```

---

# 32. Functional Workflow Example — Leave

```text
Employee
   │
   ▼
Create Leave Request
   │
   ▼
Validate Request
   │
   ▼
Submit
   │
   ▼
Line Manager
   │
   ├── Reject ─────────► Rejected
   │
   ▼
Approve
   │
   ▼
HR Manager
   │
   ├── Reject ─────────► Rejected
   │
   ▼
Approve
   │
   ▼
Approved
   │
   ▼
Update Leave Balance
```

---

# 33. Functional Workflow Example — Payroll

```text
Payroll Manager
      │
      ▼
Select Company
      │
      ▼
Select Payroll Period
      │
      ▼
Select Employees
      │
      ▼
Load Salary Structure
      │
      ▼
Apply Payroll Rules
      │
      ▼
Calculate Payroll
      │
      ▼
Review
      │
      ├── Correct / Recalculate
      │
      ▼
Finalize
      │
      ▼
Generate Payslips
      │
      ▼
PDF / Reports
```

---

# 34. Functional Workflow Example — Attendance

```text
Employee
   │
   ▼
Check In
   │
   ▼
Open Attendance
   │
   ▼
Work
   │
   ▼
Check Out
   │
   ▼
Calculate Worked Hours
   │
   ▼
Attendance History
   │
   ├── Dashboard
   ├── Reports
   └── Payroll Input
```

---

# 35. Initial Release Priorities

## Must Have

- Multi-company
- Authentication
- Role-based access
- Employee management
- Departments
- Job positions
- Line managers
- Employee self-service basics
- Web attendance
- Manual attendance
- Leave types
- Leave requests
- Manager + HR approval
- Payroll rules
- Salary structures
- Payroll processing
- Payslips
- Basic dashboard
- Basic reports
- PDF reports
- Search/filtering
- Audit fundamentals

## Should Have

- Overtime
- Manager dashboard
- Employee dashboard
- Recruitment
- Additional report filters
- CSV export

## Future

- Biometric devices
- Mobile application
- GPS attendance
- Performance management
- Training
- Expense management
- AI HR analytics

---

# 36. Functional Acceptance

A functional requirement shall be considered complete when:

- Required backend functionality exists.
- Required API endpoints are implemented.
- Required frontend interface exists.
- Validation is implemented.
- Authorization is enforced.
- Acceptance criteria are satisfied.
- Relevant automated tests pass.
- Documentation reflects actual behavior.

---

# 37. Traceability

Functional requirements shall remain traceable to:

```text
Business Requirement
        ↓
User Story
        ↓
Functional Requirement
        ↓
Technical Design
        ↓
Development Task
        ↓
Test Case
```

A requirements traceability matrix may be introduced later.

---

# 38. Document Governance

This FRD represents the current functional baseline for TechQube HRM.

Changes may occur as:

- User stories are refined.
- Technical constraints are identified.
- Business requirements change.
- Sprint feedback is collected.

Significant scope changes should be reflected in:

- BRD where business scope changes
- User Story Catalog
- FRD
- SRS
- Sprint Backlog

---

# 39. Document Status

**Version:** 1.0  
**Status:** Draft

The document will be reviewed before being baselined.
