# Postmortem: Redcrow Outage on Aug 20, 2023

# Issue Summary

**Duration:** June 20, 2024, 4:00 PM - 7:00 PM UTC (3 hours)

**Impact:** [Redcrow](http://redcrow.kz) web application
was completely unavailable to all users. Approximately 95% of users
experienced service interruptions, with the remaining 5% facing
significant slowdowns and partial functionality loss.

**Root Cause:** A misconfigured database replication process caused a
cascading failure, leading to the entire web stack becoming
unresponsive.

# Timeline

-   **4:00 PM UTC:** Monitoring alert triggered due to increased error rates on the main web application.

-   **4:05 PM UTC:** Engineer on call noticed the alert and began initial investigation.

-   **4:10 PM UTC:** Error logs indicated database connection timeouts; assumption was a database overload.

-   **4:20 PM UTC:** Misleading path: team checked for DDoS attack due to sudden spike in traffic metrics.

-   **4:45 PM UTC:** Escalated to the database administration team after initial investigations suggested database issues.

-   **5:00 PM UTC:** Database replication logs reviewed, revealing potential configuration issues.

-   **5:15 PM UTC:** Misleading path: attempted to reboot database servers, which did not resolve the issue.

-   **5:45 PM UTC:** Deep dive into replication settings; discovered misconfiguration causing primary-secondary sync failures.

-   **6:00 PM UTC:** Disabled replication temporarily and reverted to a previous stable configuration.

-   **6:30 PM UTC:** Web application services restarted and monitored for stability.

-   **7:00 PM UTC:** Full service restored and verified.

# Root Cause and Resolution

**Root Cause:** The root cause of the outage was a misconfiguration in
the database replication setup. A recent change intended to improve
replication speed inadvertently set an incorrect parameter, leading to a
desynchronization between the primary and secondary databases. This
desynchronization caused the primary database to become overwhelmed with
requests, unable to process queries efficiently, and resulting in
widespread application timeouts and failures.

**Resolution:**

1.  The replication process was disabled to stop the immediate sync issues.

2.  The incorrect parameter was identified and corrected in the configuration.

3.  The database was reverted to a stable state from backups prior to the misconfiguration.

4.  The web application and database services were restarted to ensure all connections were reset and operating correctly.

5.  Continuous monitoring was put in place to observe the system's performance post-recovery.

# Corrective and Preventative Measures

### **Improvements and Fixes**

-   **Review and Revise Database Configuration Processes:** Ensure all
    changes to critical systems like the database replication settings undergo thorough review and testing in a staging environment before being applied to production.

-   **Enhanced Monitoring:** Implement more granular monitoring for
    database performance metrics to catch issues like replication lag or configuration mismatches earlier.

-   **Documentation and Training:** Update documentation to reflect the correct replication settings and conduct training sessions for the engineering team on database configuration best practices.

### **Task List**

1.  **Patch Database Servers:** Apply the correct configuration settings
    and thoroughly test them in a non-production environment.

2.  **Implement Replication Monitoring:** Add detailed monitoring and
    alerting for replication status and performance metrics.

3.  **Update Configuration Management:** Revise configuration management
    policies to include peer review and mandatory testing for all database-related changes.

4.  **Conduct Incident Response Drills:** Regularly simulate similar
    outages to improve team response times and troubleshooting accuracy.

5.  **Review Backup Procedures:** Ensure backup processes are robust and tested regularly to facilitate quick recovery in case of configuration errors.

