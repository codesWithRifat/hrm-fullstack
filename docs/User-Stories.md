# TechQube HRM — User Story Catalog

## Document Information

| Field | Value |
|---|---|
| Project | TechQube HRM |
| Company | TechQube |
| Document | User Story Catalog |
| Version | 1.0 |
| Status | Draft |
| Methodology | Agile |
| Related Document | BRD v1.0 |

---

## 1. Purpose

This document converts the high-level business requirements defined in the TechQube HRM Business Requirements Document into user-focused requirements.

Each user story describes:

- Who needs the feature
- What the user wants to accomplish
- Why the feature provides business value
- Acceptance criteria
- Priority
- Related business requirement

Detailed functional behavior will be defined later in the Functional Requirements Document (FRD).

---

## 2. Priority Classification

The project uses MoSCoW prioritization.

| Priority | Meaning |
|---|---|
| Must Have | Required for the targeted release |
| Should Have | Important but not critical |
| Could Have | Useful enhancement |
| Won't Have | Not planned for the current release |

---

# Epic 1 — Multi-Company Management

## US-COMP-001 — Access Authorized Companies

**As an** authorized user,  
**I want** access to one or more companies,  
**so that** I can perform HR activities for the companies assigned to me.

### Acceptance Criteria

- A user can be assigned access to one or more companies.
- A user must not access unauthorized companies.
- Company-specific records must remain logically separated.
- Access rules must apply to reports and dashboards.
- Payroll information must respect company access.

**Priority:** Must Have  
**Related BR:** BR-001

---

## US-COMP-002 — Switch Active Company

**As a** multi-company user,  
**I want** to switch my active company,  
**so that** I can work with records belonging to the correct organization.

### Acceptance Criteria

- The user can see allowed companies.
- The active company is clearly indicated.
- Newly created records default to the active company.
- Unauthorized companies cannot be selected.

**Priority:** Must Have  
**Related BR:** BR-001

---

## US-COMP-003 — Company-Specific Configuration

**As an** administrator,  
**I want** HR settings to be configurable per company,  
**so that** different companies can follow different policies.

### Acceptance Criteria

- Companies may have different HR configuration.
- Leave configuration may differ by company.
- Payroll configuration may differ by company.
- Reports must use the selected company's configuration.

**Priority:** Must Have  
**Related BR:** BR-001

---

# Epic 2 — Authentication & User Access

## US-AUTH-001 — User Login

**As a** system user,  
**I want** to log in securely,  
**so that** I can access authorized HRM functions.

### Acceptance Criteria

- The user can log in using valid credentials.
- Invalid credentials are rejected.
- Successful login creates an authenticated session/token.
- Disabled users cannot log in.

**Priority:** Must Have  
**Related BR:** BR-011

---

## US-AUTH-002 — User Logout

**As a** logged-in user,  
**I want** to log out,  
**so that** my session can be securely ended.

### Acceptance Criteria

- A logout option is available.
- The current session/token is invalidated where applicable.
- Protected pages are inaccessible after logout.

**Priority:** Must Have  
**Related BR:** BR-011

---

## US-AUTH-003 — Role-Based Access

**As an** administrator,  
**I want** users to have roles and permissions,  
**so that** access to sensitive HR functions can be controlled.

### Acceptance Criteria

- Users can have defined roles.
- Roles determine allowed functionality.
- Unauthorized actions are rejected by the backend.
- Hiding frontend buttons alone must not provide security.

**Priority:** Must Have  
**Related BR:** BR-011

---

## US-AUTH-004 — Manage Users

**As an** administrator,  
**I want** to create, activate, deactivate, and manage users,  
**so that** system access can be controlled.

**Priority:** Must Have  
**Related BR:** BR-011

---

# Epic 3 — Employee Management

## US-EMP-001 — Create Employee

**As an** HR Manager,  
**I want** to create an employee record,  
**so that** the employee can be managed through the HRM system.

### Acceptance Criteria

- Required employee information must be validated.
- Employee ID must be unique within the applicable company.
- Employee must belong to a company.
- Department can be assigned.
- Job position can be assigned.
- Line manager can be assigned.
- Successful creation displays confirmation.

**Priority:** Must Have  
**Related BR:** BR-002

---

## US-EMP-002 — View Employee List

**As an** authorized HR user,  
**I want** to view employees,  
**so that** I can quickly access workforce information.

### Acceptance Criteria

- Employees are displayed in a structured list.
- Company access rules are respected.
- Archived employees can be excluded by default.
- Pagination is supported when required.

**Priority:** Must Have  
**Related BR:** BR-002

---

## US-EMP-003 — View Employee Profile

**As an** authorized user,  
**I want** to view an employee's profile,  
**so that** I can review employee information.

**Priority:** Must Have  
**Related BR:** BR-002

---

## US-EMP-004 — Update Employee

**As an** authorized HR user,  
**I want** to update employee information,  
**so that** employee records remain accurate.

**Priority:** Must Have  
**Related BR:** BR-002

---

## US-EMP-005 — Archive Employee

**As an** HR Manager,  
**I want** to archive employees who have left the organization,  
**so that** historical records remain available without treating them as active employees.

### Acceptance Criteria

- Employee records are not permanently deleted during normal HR operations.
- Archived employees do not appear in active employee lists by default.
- Historical reports may include archived employees.

**Priority:** Must Have  
**Related BR:** BR-002, BR-015

---

## US-EMP-006 — Search Employees

**As an** HR user,  
**I want** to search employees,  
**so that** I can quickly find specific records.

### Acceptance Criteria

Search should support appropriate fields such as:

- Employee ID
- Employee name
- Email
- Department
- Job position
- Company

**Priority:** Must Have  
**Related BR:** BR-016

---

## US-EMP-007 — Filter Employees

**As an** HR user,  
**I want** to filter employees,  
**so that** I can analyze specific workforce groups.

**Priority:** Should Have  
**Related BR:** BR-016

---

# Epic 4 — Employee Self-Service

## US-ESS-001 — View My Profile

**As an** employee,  
**I want** to view my employee profile,  
**so that** I can verify my personal and employment information.

**Priority:** Must Have  
**Related BR:** BR-002

---

## US-ESS-002 — View My Attendance

**As an** employee,  
**I want** to view my attendance records,  
**so that** I can identify missing or incorrect attendance.

**Priority:** Must Have  
**Related BR:** BR-005

---

## US-ESS-003 — View My Leave Balance

**As an** employee,  
**I want** to view my leave balances,  
**so that** I know how much leave is available.

**Priority:** Must Have  
**Related BR:** BR-006

---

## US-ESS-004 — View My Leave Requests

**As an** employee,  
**I want** to view my leave request history and approval status,  
**so that** I know whether my requests are pending, approved, or rejected.

**Priority:** Must Have  
**Related BR:** BR-006, BR-007

---

## US-ESS-005 — View My Payslips

**As an** employee,  
**I want** to view my payslips,  
**so that** I can review salary calculations.

**Priority:** Must Have  
**Related BR:** BR-009

---

## US-ESS-006 — Download Payslip

**As an** employee,  
**I want** to download my payslip in PDF format,  
**so that** I can retain an official salary record.

**Priority:** Must Have  
**Related BR:** BR-014

---

# Epic 5 — Organization Structure

## US-ORG-001 — Create Department

**As an** HR Manager,  
**I want** to create departments,  
**so that** employees can be organized according to company structure.

**Priority:** Must Have  
**Related BR:** BR-003

---

## US-ORG-002 — Assign Department Manager

**As an** HR Manager,  
**I want** to assign a manager to a department,  
**so that** managerial responsibility is defined.

**Priority:** Must Have  
**Related BR:** BR-003

---

## US-ORG-003 — Create Job Position

**As an** HR Manager,  
**I want** to create job positions,  
**so that** employees can be assigned appropriate organizational roles.

**Priority:** Must Have  
**Related BR:** BR-004

---

## US-ORG-004 — Assign Line Manager

**As an** HR Manager,  
**I want** to assign a line manager to an employee,  
**so that** reporting and approval workflows can follow the organization hierarchy.

**Priority:** Must Have  
**Related BR:** BR-003, BR-007

---

# Epic 6 — Manager Self-Service

## US-MGR-001 — View My Team

**As a** line manager,  
**I want** to view employees reporting to me,  
**so that** I can manage my team.

**Priority:** Must Have  
**Related BR:** BR-003

---

## US-MGR-002 — View Team Attendance

**As a** line manager,  
**I want** to review my team's attendance,  
**so that** I can monitor attendance issues.

**Priority:** Should Have  
**Related BR:** BR-005

---

## US-MGR-003 — View Team Leave

**As a** line manager,  
**I want** to view team leave information,  
**so that** I can plan team availability.

**Priority:** Must Have  
**Related BR:** BR-006

---

# Epic 7 — Attendance

## US-ATT-001 — Web Check-In

**As an** employee,  
**I want** to check in using the HRM web application,  
**so that** my attendance start time is recorded.

### Acceptance Criteria

- Only authenticated employees can check in.
- Check-in time is recorded.
- Duplicate active check-ins are prevented.
- Company and employee information are associated with the attendance record.

**Priority:** Must Have  
**Related BR:** BR-005

---

## US-ATT-002 — Web Check-Out

**As an** employee,  
**I want** to check out,  
**so that** my working time can be calculated.

**Priority:** Must Have  
**Related BR:** BR-005

---

## US-ATT-003 — Manual Attendance Entry

**As an** HR Manager,  
**I want** to manually create attendance records,  
**so that** valid attendance can be recorded when automatic check-in is unavailable.

**Priority:** Must Have  
**Related BR:** BR-005

---

## US-ATT-004 — Correct Attendance

**As an** authorized HR user,  
**I want** to correct incorrect attendance records,  
**so that** HR and payroll information remains accurate.

**Priority:** Must Have  
**Related BR:** BR-005

---

## US-ATT-005 — Detect Missing Check-Out

**As an** HR Manager,  
**I want** to identify incomplete attendance records,  
**so that** missing check-outs can be corrected.

**Priority:** Should Have  
**Related BR:** BR-005

---

## US-ATT-006 — Calculate Working Hours

**As an** HR Manager,  
**I want** employee working hours to be calculated from attendance,  
**so that** attendance and payroll calculations can use accurate worked time.

**Priority:** Must Have  
**Related BR:** BR-005

---

## US-ATT-007 — Track Overtime

**As an** HR Manager,  
**I want** to identify overtime,  
**so that** additional worked hours can be reviewed and potentially used in payroll.

**Priority:** Should Have  
**Related BR:** BR-005, BR-008

---

# Epic 8 — Leave Management

## US-LEV-001 — Configure Leave Type

**As an** HR Manager,  
**I want** to create configurable leave types,  
**so that** different leave policies can be represented.

Examples:

- Annual Leave
- Casual Leave
- Sick Leave
- Maternity Leave
- Unpaid Leave

**Priority:** Must Have  
**Related BR:** BR-006

---

## US-LEV-002 — Configure Leave Allocation

**As an** HR Manager,  
**I want** to define leave entitlements,  
**so that** employees receive the correct leave balance.

**Priority:** Must Have  
**Related BR:** BR-006

---

## US-LEV-003 — Request Leave

**As an** employee,  
**I want** to submit a leave request,  
**so that** I can request authorized time away from work.

### Acceptance Criteria

- Employee selects a leave type.
- Employee selects required dates.
- System validates leave balance where applicable.
- Request enters the approval workflow.
- Employee can see request status.

**Priority:** Must Have  
**Related BR:** BR-006

---

## US-LEV-004 — Line Manager Approval

**As a** line manager,  
**I want** to approve or reject leave requests from my direct reports,  
**so that** team availability can be reviewed before HR approval.

### Acceptance Criteria

- Manager sees requests awaiting their approval.
- Manager can approve.
- Manager can reject.
- Rejection requires a reason.
- Approved requests move to HR Manager.

**Priority:** Must Have  
**Related BR:** BR-007

---

## US-LEV-005 — HR Manager Approval

**As an** HR Manager,  
**I want** to provide final approval for leave requests,  
**so that** HR policies are enforced.

### Acceptance Criteria

- HR Manager sees requests approved by the line manager.
- HR Manager can approve or reject.
- Final approval updates leave status and balance.

**Priority:** Must Have  
**Related BR:** BR-007

---

## US-LEV-006 — Handle Missing Line Manager

**As an** HR Manager,  
**I want** leave requests without an assigned line manager to route appropriately,  
**so that** requests do not become blocked.

### Acceptance Criteria

- If no line manager exists, the request may route directly to HR Manager according to configuration.

**Priority:** Must Have  
**Related BR:** BR-007

---

# Epic 9 — Payroll

## US-PAY-001 — Create Payroll Rule

**As a** Payroll Manager,  
**I want** to create payroll rules,  
**so that** salary calculations can adapt to company policies.

Examples:

- Basic Salary
- House Rent
- Medical Allowance
- Overtime
- Bonus
- Tax
- Provident Fund
- Loan Deduction

**Priority:** Must Have  
**Related BR:** BR-008

---

## US-PAY-002 — Configure Payroll Rule

**As a** Payroll Manager,  
**I want** to configure how a payroll rule is calculated,  
**so that** salary calculations do not require source-code modification.

### Rule information may include

- Rule name
- Rule code
- Category
- Sequence
- Calculation method
- Fixed amount
- Percentage
- Calculation base
- Conditions
- Active status

**Priority:** Must Have  
**Related BR:** BR-008

---

## US-PAY-003 — Create Salary Structure

**As a** Payroll Manager,  
**I want** to group payroll rules into salary structures,  
**so that** different employee groups can use different compensation schemes.

**Priority:** Must Have  
**Related BR:** BR-008

---

## US-PAY-004 — Assign Salary Structure

**As a** Payroll Manager,  
**I want** to assign a salary structure to an employee,  
**so that** the correct payroll rules are used.

**Priority:** Must Have  
**Related BR:** BR-008

---

## US-PAY-005 — Process Payroll

**As a** Payroll Manager,  
**I want** to run payroll for a payroll period,  
**so that** employee salaries can be calculated.

**Priority:** Must Have  
**Related BR:** BR-009

---

## US-PAY-006 — Review Payroll Calculation

**As a** Payroll Manager,  
**I want** to review calculated salary components before finalization,  
**so that** payroll errors can be detected.

**Priority:** Must Have  
**Related BR:** BR-009

---

## US-PAY-007 — Finalize Payroll

**As a** Payroll Manager,  
**I want** to finalize payroll,  
**so that** completed payroll records are protected from accidental modification.

**Priority:** Must Have  
**Related BR:** BR-009, BR-015

---

## US-PAY-008 — Generate Payslip

**As a** Payroll Manager,  
**I want** to generate payslips,  
**so that** employees receive a breakdown of salary calculations.

**Priority:** Must Have  
**Related BR:** BR-009

---

# Epic 10 — Recruitment

## US-REC-001 — Create Job Vacancy

**As an** HR or Recruitment Officer,  
**I want** to create job vacancies,  
**so that** open positions can be tracked.

**Priority:** Should Have  
**Related BR:** BR-010

---

## US-REC-002 — Register Candidate

**As a** Recruitment Officer,  
**I want** to register candidates,  
**so that** applicant information can be managed.

**Priority:** Should Have  
**Related BR:** BR-010

---

## US-REC-003 — Manage Recruitment Stages

**As a** Recruitment Officer,  
**I want** to move applicants through recruitment stages,  
**so that** recruitment progress can be tracked.

Example stages:

- New
- Screening
- Interview
- Offer
- Hired
- Rejected

**Priority:** Should Have  
**Related BR:** BR-010

---

## US-REC-004 — Schedule Interview

**As a** Recruitment Officer,  
**I want** to record interview schedules,  
**so that** candidate interviews can be coordinated.

**Priority:** Should Have  
**Related BR:** BR-010

---

## US-REC-005 — Hire Candidate

**As an** HR Manager,  
**I want** to convert a successful candidate into an employee,  
**so that** recruitment information can flow into employee management.

**Priority:** Should Have  
**Related BR:** BR-010

---

# Epic 11 — Dashboard & Analytics

## US-DASH-001 — HR Dashboard

**As an** HR Manager,  
**I want** a dashboard with important HR indicators,  
**so that** I can understand workforce status quickly.

### Initial Dashboard Metrics

- Total Employees
- Active Employees
- New Joiners
- Employees by Company
- Employees by Department
- Present Today
- Absent Today
- Employees on Leave Today
- Pending Leave Requests
- Upcoming Birthdays
- Open Vacancies

**Priority:** Must Have  
**Related BR:** BR-012

---

## US-DASH-002 — Manager Dashboard

**As a** line manager,  
**I want** a team dashboard,  
**so that** I can quickly understand my team's HR status.

### Initial Metrics

- Team Headcount
- Team Present Today
- Team Absent Today
- Team Members on Leave
- Pending Approvals

**Priority:** Should Have  
**Related BR:** BR-012

---

## US-DASH-003 — Employee Dashboard

**As an** employee,  
**I want** a personal dashboard,  
**so that** I can quickly access my HR information.

### Initial Information

- Attendance status
- Leave balance
- Pending requests
- Recent attendance
- Latest payslip

**Priority:** Should Have  
**Related BR:** BR-012

---

# Epic 12 — Reports

## US-RPT-001 — Employee List Report

**As an** HR Manager,  
**I want** an employee report,  
**so that** workforce information can be reviewed and exported.

**Priority:** Must Have  
**Related BR:** BR-013

---

## US-RPT-002 — Headcount Report

**As an** HR Manager,  
**I want** headcount reports by company and department,  
**so that** workforce distribution can be analyzed.

**Priority:** Must Have  
**Related BR:** BR-013

---

## US-RPT-003 — Attendance Report

**As an** HR Manager,  
**I want** attendance reports by date range, employee, department, and company,  
**so that** attendance performance can be analyzed.

**Priority:** Must Have  
**Related BR:** BR-013

---

## US-RPT-004 — Leave Report

**As an** HR Manager,  
**I want** leave reports,  
**so that** leave usage and balances can be analyzed.

**Priority:** Must Have  
**Related BR:** BR-013

---

## US-RPT-005 — Payroll Summary

**As a** Payroll Manager,  
**I want** payroll summary reports,  
**so that** salary costs and payroll components can be reviewed.

**Priority:** Must Have  
**Related BR:** BR-013

---

## US-RPT-006 — Recruitment Report

**As a** Recruitment Officer,  
**I want** recruitment reports,  
**so that** vacancy and candidate progress can be analyzed.

**Priority:** Should Have  
**Related BR:** BR-013

---

# Epic 13 — PDF Documents

## US-PDF-001 — Employee Profile PDF

**As an** HR Manager,  
**I want** to generate an employee profile PDF,  
**so that** employee information can be printed or shared appropriately.

**Priority:** Should Have  
**Related BR:** BR-014

---

## US-PDF-002 — Attendance PDF

**As an** HR Manager,  
**I want** attendance reports in PDF format,  
**so that** official attendance reports can be retained.

**Priority:** Must Have  
**Related BR:** BR-014

---

## US-PDF-003 — Leave PDF

**As an** HR Manager,  
**I want** leave reports and approval information in PDF format,  
**so that** leave records can be printed or retained.

**Priority:** Should Have  
**Related BR:** BR-014

---

## US-PDF-004 — Payslip PDF

**As an** employee,  
**I want** to download my payslip as PDF,  
**so that** I have an official salary document.

**Priority:** Must Have  
**Related BR:** BR-014

---

## US-PDF-005 — Payroll Summary PDF

**As a** Payroll Manager,  
**I want** payroll summaries in PDF format,  
**so that** payroll results can be reviewed or shared with authorized stakeholders.

**Priority:** Must Have  
**Related BR:** BR-014

---

# Epic 14 — Search, Filtering & Data Navigation

## US-SRCH-001 — Search Major Records

**As a** system user,  
**I want** to search major records,  
**so that** I can find information efficiently.

**Priority:** Must Have  
**Related BR:** BR-016

---

## US-SRCH-002 — Filter Reports

**As an** HR user,  
**I want** to filter reports by relevant criteria,  
**so that** I can analyze specific information.

Potential filters include:

- Company
- Department
- Employee
- Date range
- Status

**Priority:** Must Have  
**Related BR:** BR-016

---

## US-SRCH-003 — Sort Records

**As a** system user,  
**I want** to sort records,  
**so that** information can be organized meaningfully.

**Priority:** Should Have  
**Related BR:** BR-016

---

# Epic 15 — Audit & Data Integrity

## US-AUD-001 — Record Important Changes

**As an** auditor or administrator,  
**I want** important HR changes to be traceable,  
**so that** the organization can review what changed and who changed it.

**Priority:** Must Have  
**Related BR:** BR-015

---

## US-AUD-002 — Protect Finalized Payroll

**As a** Payroll Manager,  
**I want** finalized payroll records protected from silent changes,  
**so that** payroll history remains reliable.

**Priority:** Must Have  
**Related BR:** BR-015

---

## US-AUD-003 — Preserve Archived Records

**As an** HR Manager,  
**I want** archived employee information retained,  
**so that** historical HR reports remain accurate.

**Priority:** Must Have  
**Related BR:** BR-015

---

# Epic 16 — Future Backlog

These stories are intentionally outside the initial implementation scope but may be considered in future releases.

## US-FUT-001 — Biometric Attendance Integration

**As an** HR Manager,  
**I want** attendance devices integrated with the HRM,  
**so that** biometric attendance can be synchronized automatically.

**Priority:** Won't Have — Initial Release

---

## US-FUT-002 — GPS Mobile Attendance

**As an** organization,  
**I want** employees to check in from approved geographical locations,  
**so that** remote/mobile attendance can be controlled.

**Priority:** Won't Have — Initial Release

---

## US-FUT-003 — Performance Management

**As an** HR Manager,  
**I want** employee performance and appraisal functionality,  
**so that** employee performance can be tracked.

**Priority:** Won't Have — Initial Release

---

## US-FUT-004 — Training Management

**As an** HR Manager,  
**I want** employee training records,  
**so that** learning and development can be managed.

**Priority:** Won't Have — Initial Release

---

## US-FUT-005 — Expense Management

**As an** employee,  
**I want** to submit business expenses,  
**so that** eligible expenses can be reimbursed.

**Priority:** Won't Have — Initial Release

---

## US-FUT-006 — Mobile Application

**As an** employee,  
**I want** a mobile application,  
**so that** I can access HR services from my mobile device.

**Priority:** Won't Have — Initial Release

---

# 17. User Story Summary

| Epic | Area |
|---|---|
| 1 | Multi-Company |
| 2 | Authentication & Access |
| 3 | Employee Management |
| 4 | Employee Self-Service |
| 5 | Organization Structure |
| 6 | Manager Self-Service |
| 7 | Attendance |
| 8 | Leave |
| 9 | Payroll |
| 10 | Recruitment |
| 11 | Dashboard |
| 12 | Reports |
| 13 | PDF Documents |
| 14 | Search & Filtering |
| 15 | Audit & Data Integrity |
| 16 | Future Backlog |

---

# 18. Backlog Refinement Policy

Not every story in this document will be implemented immediately.

Before a story enters a development sprint, it should be refined to include:

- Confirmed business requirement
- Detailed acceptance criteria
- UI requirements where applicable
- API requirements where applicable
- Database impact
- Security considerations
- Testing requirements
- Dependencies
- Estimated complexity

---

# 19. Definition of Ready

A story may enter a sprint when:

- The business objective is understood.
- Acceptance criteria are clear.
- Major dependencies are identified.
- Required designs are sufficiently understood.
- The development team can estimate the work.

---

# 20. Definition of Done

A story is considered complete when applicable criteria are satisfied:

- Implementation completed
- Acceptance criteria satisfied
- Input validation implemented
- Authorization implemented
- Backend tests completed
- Frontend tests completed
- Integration tested
- Documentation updated
- Code reviewed
- No known critical defects
- Pull request merged

---

# 21. Document Status

**Version:** 1.0  
**Status:** Draft

This backlog will continue to evolve throughout Agile development.

Stories may be added, refined, reprioritized, split, or removed as business requirements become clearer.