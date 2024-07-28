# Change Log
CodeTogether is available for VS Code, Eclipse, and IntelliJ providing pair programming services right from a browser.

## [2024.3.1] - 2024.7.23
- **On-Premises IntelliJ Client Fixes**  
  Fixed a problem with syntax highlighting when joining a session from IntelliJ in on-premises deployments..
- **Audio and Video Fixes**  
  Resolved an issue with audio and video not working when joining from a browser.
- **Security Vulnerability Fixes**  
  Patched identified security vulnerabilities across various components, enhancing the overall security posture of the platform.

## [2024.3.0] - 2024.6.19
- **IntelliJ Fixes**  
  Resolved a few issues with IntelliJ including oddities when using IntelliJ as a client editing very small files across OSes resulting in potential lost changes.
- **Security Vulnerability Fixes**  
  Patched identified security vulnerabilities across various components, enhancing the overall security posture of the platform.
- **Docker Container Updates**  
  Upgraded services on the on-premises backend container, ensuring compatibility with latest libraries.

## [2024.2.0] - 2024.3.26
- **VS Code Sync Issue Resolution**  
  Resolved critical issues in VS Code that could lead to getting into out-of-sync state during code editing.
- **VS Code Client Outline**  
  Resolved issue in changes with the symbol provider fixing VS Code outline in client sessions.
- **Security Vulnerability Fixes**  
  Patched identified security vulnerabilities across various components, enhancing the overall security posture of the platform.
- **OpenEdge ABL Support**  
  Added support for syntax coloring for OpenEdge ABL language.
- **Migration from Gitter to GitHub**  
  Discontinued the use of Gitter for streamlined communication and community engagement on GitHub.
- **Enhanced Session Stability**  
  Implemented improvements to handle unstable sessions more effectively across different IDE clients, enhancing overall reliability.

## [2024.1.0] - 2024.1.16
- **CodeTogether Live Branding**  
  With the introduction of CodeTogether HQ, the CodeTogether extensions have now been rebranded to CodeTogether Live. Use both Live and HQ to significantly streamline your DevOps operations.
- **New SaaS Infrastructure**  
  New for 2024 is a completely rebuilt SaaS infrastructure that is more scalable and reliable than ever before. This infrastructure provides lower latency sessions as well as stable regional URLs that simplifies whitelisting.
- **IntelliJ Compatibility**  
  The latest release of IntelliJ had API changes impacting certain functionality. This release addresses all issues ensuring a smooth experience for collaboration including propogation of edits and clear collaboration status.
- **Eclipse Compatibility**  
  The latest release of Eclipse had API changes that also impacted functionality. This release fixes issues with syntax coloring as a guest, and includes other fixes to smooth out the editing experience.
- **General Fixes**  
  This release of CodeTogether Live has a series of general fixes included in it from optimizing memory usage, to improving CA in old versions of IDEs, and more. Thanks for the reports!
- **Security Fixes**  
  Beyond bug fixes, this release updates a number of third-party libraries addressing detected security vulnerabilities in those libraries.

## [2023.2.0] - 2023.9.20
- **Session Restoration by IDE Clients**  
  Introduced support for IDE clients to automatically restore session connections, ensuring minimal disruptions.
- **IntelliJ 2023.2 Compatibility**  
  Enhanced compatibility with IntelliJ 2023.2 ensuring smooth operation and bug-free experience.
- **VS Code Secret Storage Migration**  
  Started to use Secret Storage API within the VS Code environment for storing sensitive data.
- **Security Vulnerability Mitigations**  
  Updated components in the CodeTogether container for On-Premises deployments to pick up the latest security fixes.

## [2023.1.1] - 2023.4.19
- **VS Code Hosting and Teams**  
  For CodeTogether Team users on VS Code, certain users would experience problems with guests authenticating to the session. This has been fixed.
- **IntelliJ 2023.1 Compatibility**  
  With the 2023.1 release of Jetbrains IDEs, fixed compatibility with API changes ensuring a guest's ability to view terminals.

## [2023.1.0] - 2023.3.22
- **Output for Tests in IntelliJ**  
  Clients now see missing content from the test execution output from IntelliJ host.
- **Kotlin Tests not Visible**  
  When using IntelliJ 2022.2+, guests can now see and execute Kotlin tests.
- **JetBrains Gateway**  
  Various issues in Gateway addressed, including an inability to join the session and A/V icons being broken.
- **Large Files**  
  Files larger than 16mb are now not available for opening on clients as doing so could break the session experience.
- **Server Sharing**  
  Server/port sharing is now simpler including automatic sharing of a restarted server.
- **Files Out of Sync**  
  Fixed an edge case on the VS Code host which could stop changes being applied to the shared file.
- **Verify Guests by Pairing Codes**  
  Now when joining a session, guests are prompted to enter a pairing code to verify their identity. This is a security feature to prevent guests from joining a session without the host's knowledge.
- **Security Fixes**  
  Several dependency updates to fix security vulnerabilities.

## [2022.2.3] - 2022.12.14
- **IntelliJ 2022.3**  
  Fixes compatibility issues with the IntelliJ 2022.3 release.
- **On-Premises Fixes**  
  Addressed permission issues in OpenShift deployment and added support for a periodic CodeTogether server restart in the container.
- **On-Premises SSO Fixes**  
  Fixes for problems with SSO authentication when joining session from a browser and when using Safari as a default browser with 'prevent cross-site tracking' enabled.
- **Security Fixes**  
  Dependencies updated to fix security vulnerabilities.

## [2022.2.2] - 2022.9.14
- **Eclipse 2022-09**  
  Fixes compatibility issues with the upcoming Eclipse 2022-09 release.
- **Security Fixes**  
  Updated SSL certs and minor security vulnerabilities addressed.
- **Miscellaneous Fixes**  
  Fixes for proposed APIs, On-Premises SSO integration and several other issues.

## [2022.2.1] - 2022.7.4
- **Inline Search in VS Code**  
  Participants now follow a VS Code host navigating through source code using inline search.
- **Better Updates in VS Code**  
  Getting updates in VS Code is now more clearer with optional or mandatory updates clearly visualized and actionable.
- **On-Premises Security Updates**  
  This release updates a series of packages and modules that while not causing a direct exploitable vulnerability are known to have moderate-severity security issues.
- **On-Premises SSO Fixes**  
  To ensure compatibility, fixes an issue with connecting to specific SSO providers regarding payload format.
- **On-Premises Read-only Filesystem**  
  As part of a security theme, CodeTogether's On-Premises image now supports running as a read-only file system.

## [2022.2.0] - 2022.6.16
- **Force to Follow**  
  Hosts and guests now have the ability to bring everyone to their location with the new 'Force all to follow' action. To avoid abuse in larger sessions, guests do not have this option if more than 3 guests.
- **Terminals Focus on Host**  
  When remote participants have been granted access and are interacting with a terminal, on the host side the terminal is automatically focused during input to allow the host to track activity. This focus behavior can be turned off in preferences.
- **Follow vs. Watch**  
  To help improve usability for new users, CodeTogether now uses Follow language instead of Watch as well as being exposed more clearly in one-on-one sessions.
- **Refresh Account from View**  
  For users who have recently purchased, there is now an option to 'Recheck Access' to Pro or Teams for cases where the IDE has not auto-detected the purchase.
- **Eclipse 2022-06 Compatibility**  
  Addresses an incompatibility with Eclipse 2022-06 to ensure clean installation on all versions of Eclipse.
- **On-Premises Improvements**  
  Multiple improvements for on-premises customers including being able to use SSL database connections without specific certs, Helm chart clean-up, and additional validation of inconsistent configuration values.

## [2022.1.6] - 2022.5.24
- **Compatibility Fixes**  
  A couple small but impactful fixes were identified in 2022.1.5 including an issue enabling proposed APIs in VS Code that have been addressed.

## [2022.1.5] - 2022.5.18
- **IntelliJ Performance Fixes**  
  Addressed an issue reported by several users that could result in high-CPU usage when starting consecutive sessions in IntelliJ.
- **Better Test Output Support**  
  More complete test output, including output for passed tests, is available for sessions hosted in IntelliJ.
- **SSL Support for Database Connection in Locator Mode**  
  Locator allows users to use a secured connection with the database in the Locator mode.
- **Miscellaneous Fixes**  
  Some other fixes across all supported platforms to improve the quality.

## [2022.1.4] - 2022.4.4
- **Joining from VS Code Fixes**  
  Fixed an odd issue for joining sessions from VS Code clients to ensure consistent behavior.
- **Quick Open Improved in Browser**  
  When using quick open, the browser will now handle local fuzzy matching of results as a search is refined.
- **Miscellaneous Fixes**  
  A few other fixes landed as part of our continual effort to improve quality of coding sessions.

## [2022.1.3] - 2022.3.21
- **Kotlin Test Support in IntelliJ**  
  When working with Kotlin tests, CodeTogether will now relay results run on IntelliJ hosts to remote clients.
- **Eclipse Wild Web Developer Support**  
  CodeTogether now supports most language features exposed from Eclipse's Wild Web Developer's language servers including remote quick fixes.
- **GitPod Compatible**  
  CodeTogether can now be fully used inside a GitPod environment enabling remote collaboration simply by enabling the extension from the marketplace.
- **Docker Image Enhancements**  
  The on-premises Docker image has been enhanced to simplify deployment in Fargate and Amazon allowing simpler rollout in private clouds.
- **Fixes and Fixes**  
  Continuing with stability fixes for CodeTogether, this release addresses some smaller annoyances that our users have been kind enough to report.

## [2022.1.2] - 2022.2.17
- **A/V Toolbar in JetBrains IDEs**  
  Fixed an issue for some clients where the A/V toolbar in IntelliJ may not have shown causing issues using audio and visual comunications in sessions.
- **Connections Gone Wild**  
  In an unfortunate edge case, a handful of user systems have gone wild hammering our servers. This release closes a window that could allow multiple reconnect cycles to start.
- **On-Premises Fixes**  
  This patch release addresses a few nuances for our on-premises users including enabling TLS 1.3 support and improvements to the Docker image startup to better detect and warn for irregular inputs.

## [2022.1.1] - 2022.2.8
- **More Free Usage**  
  Registration is no longer needed to unlock the free 60-minute and 3 guest plan; now all anonymous users get full Free access too!
- **Browser Keyboard Navigation**  
  You can now use Enter to navigate multiple results found when using inline search.
- **Faster VS Code Typing**  
  When processing remote events into VS Code on a loaded system, edits could fall behind. Changes are now intelligently grouped for optimal performance.
- **Virtual Cursor Improvements**  
  When joining a virtual cursor, you will immediately jump to the source without a backoff countdown.
- **Tweaks and Fixes**  
  Includes small UI tweaks and cleanup to ensure an optimal experience for CodeTogether users.
- **On-Premises :: OneLogin SSO**  
  For On-Premises customers, we have fixed a compatibility issue integrating with OneLogin for single sign-on.
- **On-Premises :: Graphs Dashboard**  
  Building on dashboard improvements, a new dashboard tab gives access to usage graphs including information on Host and Guest IDEs being used.

## [2022.1.0] - 2022.1.25
- **A New Year :: Awesome Things**  
  CodeTogether 2022.1 brings a great set of improvements from coding ease to fixes and new functionality. Oh, and a new versioning pattern too!
- **Faster Code Assistance**  
  Code completion is much faster. Heavily optimized content assist payloads and faster processing gives a local coding experience when using explicit or trigger-character assistance.
- **Smart and Explicit Driver Modes**  
  The smart driver mode in CodeTogether has been enhanced to be more natural, especially when driver changes. In addition, an explicit (strict-style) driver mode is now available for mob/pair programming sessions.
- **Progress when Joining**  
  All IDEs now visualize status during joining including indicating the chosen cursor mode. When hosts let guests choose their cursor mode, during join selection of a shared or personal cursor is now available.
- **Large Project Support**  
  Joining from IDEs now handles fully very large projects, avoiding problems with timeouts when payloads were too large given bandwidth available. Progress of metadata retrieval is now also shown when joining.
- **Rooms Renamed to Virtual Cursors**  
  The semantics around rooms have been simplified using new virtual cursor terminology to make it more direct when interacting with CodeTogether.
- **General Coding Fixes**  
  Multiple additional fixes have been made from improved application of code completion, fixing automatic trigger of content assist in some cases, and other fixes reported by users.
- **VS Code Compatibility**  
  Latest versions of VS Code changed how proposed APIs could be enabled. This release ensures maximum compatibility.
- **On-Premises Dashboard Enhancements**  
  For On-Premises customers, the Dashboard available for behind-the-firewall server has been significantly improved including supporting real-time update of metrics and audit entries.
- **On-Premises Locator Available**  
  For On-Premises customers, the CodeTogether Locator is available allowing managed regional deployments, automated load balancing and more.

## [5.0.1] - 2021.11.15
- **Building on 5.0 Audio/Video/Screensharing**  
  The 5.0.1 release builds on the newly introduced A/V support in CodeTogether 5 adding reliability and coding fixes.
- **Better Typing Collision Management**  
  An algorithmic improvement allows for increased flexilibity when typing in the same file and avoids file-sync events in more situations.
- **Simultaneous Coding Content Assist Fixes**  
  In certain situations where a peer is coding above the content assist location in a file, the content assist will now properly load and apply.
- **Shared Port Detection on Windows 11.next**  
  The removal of WMIC in Dev builds of Windows 11 impacted automatic detection of ports and now uses alternative mechanisms.
- **Various Stability Fixes**  
  5.0.1 brings fixes for intellisense after . on VS Code client, a periodic loss character issue on VS Code as well as removes possible multi-second editor freezes on IntelliJ and Eclipse.
- **On-Premises Container Fixes**  
  For CodeTogether On-Premises customers, CodeTogether's container has been updated to now work well with Podman adding to the existing support for K8s, Docker, and OpenShift.

## [5.0.0] - 2021.10.28
- **5.0 is here with Audio/Video/Screensharing!**  
  Seamless audio, video and screensharing is now available for all CodeTogether sessions. Simply click the headphone toggle to get started during a session.
- **Audio Guests Welcome**  
  As part of audio/video support, copying the URL to the audio-portion of the meeting allows you to invite non-coding guests to the call as well.
- **Better Indentation in Clients**  
  Smarts used in the CodeTogether clients have been improved for processing automatic indentation to provide a richer and more natural experience.
- **General Improvements**  
  Multiple fixes landed including improved support for remote quick fixes, more efficient relaying of error markers, Terminal integration optimizations and more.

## [4.2.0] - 2021.9.23
- **Unit Test Support Lands**  
  Session guests can now see results of unit tests invoked and if permission allows, remotely invoke tests from all clients. Results are visualized both as part of editor side bars as well as in IDE-familiar views.
- **Remotely Launch Programs**  
  Beyond tests, other programs can now be invoked remotely with the ability to stop and monitor the current invocations.
- **On-Premises Metrics Dashboard**  
  When deploying CodeTogether on-premises, a new metrics dashboard provides access to usage trends and real-time information. In addition, CodeTogether can be configured to export metrics to Prometheus and StatsD systems.
- **Numerous Fixes**  
  Continued improvements have been made across CodeTogether increasing the reliability of the system and improving the coding experience. Key fixes have also landed for server port sharing that both increase reliability and performance.

## [4.1.3] - 2021.8.19
- **Summertime Fixes (4.1.x)**  
  Ensure compatibility with latest IDE releases including VS Code 1.58+ and IntelliJ 2021.2.

## [4.1.2] - 2021.8.9
- **Summertime Fixes**  
  Optimizations for code completion payload size increasing performance, improvements for compatibility with remote system support, and fixes in On-Premises for single-signon and certificate compatibility.

## [4.1.1] - 2021.7.28
- **Summertime Fixes**  
  Compatibility fixes with latest IDE releases including VS Code 1.58 and others.

## [4.1.0] - 2021.6.29
- **Share Servers and More**  
  Now CodeTogether allows you to share your local web app under development with your peers, fully end-to-end secured. Flexible enough to handle WebSockets, database connections, or remote debug!
- **Refactor Rename**  
  You can now remotely refactor rename symbols and classes leveraging host-side language intelligence with changes reflected across all participants.
- **Open Symbol and Open Type**  
  New in 4.1, the ability to jump to types and symbols expands your ways to efficiently navigate and develop remotely.
- **Workspace-Wide Search**  
  The Eclipse and IntelliJ clients now also support full workspace-wide search. Additional fixes on the host side of all IDEs increase the reliability of searches.
- **New Java Files Improved**  
  When creating .java files remotely, CodeTogether will automatically fill in the basic class structure making it quicker to make new classes remotely.
- **Support for SAP's ABAP**  
  Advanced support for ABAP development hosting either using the VS Code or Eclipse ABAP plug-in is now available, including remote access to the Activate File lifecycle.
- **Eclipse Client Indentation**  
  Using the Eclipse client could give inconsistent indentation results depending on the version of Eclipse. This is now fully contained inside CodeTogether ensuring expected auto-indents.
- **.codetogether.ignore Glob Patterns**  
  Expanded support for .codetogether.ignore files now allows full glob pattern usage expanding ways to limit files exposed to session participants.
- **VS Code Proxy Support**  
  Various changes have been made to improve Proxy support in VS Code including respecting non-proxy hosts and detecting certain problematic configurations.
- **On-Premises Automated Updates**  
  Clients using On-Premises deployments now benefit by automated updates on all IDEs simplifying the management for end-users.
- **Remote File System Improvements**  
  Fixes for specific situations where folder and file rename/move actions could result in inconsistent state on remote clients have been implemented.
- **Anonymously Join from Guest IDEs**  
  It is no longer required to register a CodeTogether account to simply join a session from a remote guest IDE making usage even easier.
- **Session Time Limits**  
  Starting on July 15, 2021, session time limits go into effect as had been previously announced on the CodeTogether portal.
- **Easier to Join Teams**  
  When creating or joining a team on the CodeTogether portal with your IDE running with CodeTogether installed, you will be automatically signed in and have access immediately to Team benefits.

## [4.0.0] - 2021.3.23
- **Now with CodeTogether Teams**  
  The 4.0 release now includes CodeTogether Teams as an opt-in feature, improving the user experience and providing enhanced security. CodeTogether Teams greatly simplifies collaboration with team-centric flows and visualizations.
- **Write-Access in Terminals**  
  As part of a secure Team, write-access to Terminals can be enabled unlocking richer collaboration across teams.
- **Call and Type Hierarchies**  
  IDE and Browser clients can now access call and type hierarchies, even from heterogeneous hosts, improving the code navigation experience.
- **Language Smarts Enhanced**  
  From finding implementations and references, to code completion, 4.0 provides a more natural remote coding experience.
- **Warnings and Intentions Relayed**  
  Clients now will receive warning and intention markers from the host for files being edited together. A limit of 250 will be relayed per file for performance reasons.
- **Single Sign-On (SSO) for On-Premises**  
  For companies deploying CodeTogether On-Premises, SSO can now be configured using standard OAuth providers such as those from Okta and Microsoft.
- **Compatibility Fixes**  
  CodeTogether is now compatible with VSCodium and Eclipse 2021-03. Fixes address runtime issues with IBM J9 runtime and particular IntelliJ Host project module configurations.

## [3.2.0] - 2021.1.28
- **Terminal Sharing (Preview)**  
  Terminals are now shared across IDEs, providing access to more information when pairing! Access is read-only as part of this technology preview, with read-write support coming in version 3.3.
- **Better Editor Colors**  
  Syntax colors in IntelliJ and Eclipse would often fall short of expectations. This release ensures greater consistency with your chosen color theme.
- **VS Code Client Features**  
  New in this release is access to advanced VS Code features when joining remote sessions, including search in workspace, and jumping to a file using Quick Open. Overall a much more natural experience.
- **Improved Session UX**  
  The session visualization across IDEs has been improved to better visualize the state, along with available actions to manage your access to the session.

## [3.1.0] - 2020.12.8
- **Console Sharing**  
  Output and console windows are now shared letting others see directly the output of programs and unit tests, a top requested feature!
- **Who Codes? You Decide**  
  When hosting new sessions, new choices control who can edit files and drive in the session. You can now share files read-only, or be the only one driving!
- **Non-Project Files Shared**  
  External files that are not part of the project are dynamically shared when viewed on a host, making it easier to work with class libraries and other alternative sources.
- **Join Session Authorization**  
  By default CodeTogether now requires you to authorize new participants joining the session, giving you more control over who can access your source code.
- **Auto-Reconnecting Hosts**  
  Hosting sessions is now more tolerant of network glitches, automatically re-establishing connectivity and maintaining the active session.
- **Automatic Indentation Fixes**  
  A series of fixes now ensure a more consistent behavior when coding, including indents around brackets and when completing snippets.

## [3.0.1] - 2020.11.2
- **Miscelaneous Fixes**  
  Thanks for the quick feedback! A few key issues were fixed including support for connecting from behind certain proxies to remote sessions.

## [3.0.0] - 2020.10.22
- **Join from Your IDE!**  
  You now can directly connect to a remote session from inside your IDE. Use your native IDE editor, key bindings and more, even in teams with heterogeneous IDEs.
- **Simultaneous Editing**  
  You can now code together in the same file, at the same time. No longer do you need to wait for your turn to start coding.
- **Visualization of Status**  
  When working in a session, CodeTogether now visualizes if you are working together or editing alone, or even simply browsing while someone else codes.
- **Better Content Assist**  
  As part of supporting simultaneous editing, numerous fixes have landed to improve the content assist experience, including more consistent inclusion of () and trailing ;.
- **New Languages Supported**  
  Syntax coloring has been added for Ruby, YAML, LaTeX and ABAP, including support from within IDE Clients joining remote sessions.
- **What's Next?**  
  Coming in 3.1+: support for sharing terminals and console output, as well as Refactoring across IDE and Browser clients!

## [2.1.1] - 2020.8.20
- **Unreliable Network Recovery**  
  Network drops? CodeTogether now recovers cleanly including syncing missed edits from the session.
- **Lost Edits? No More**  
  Certain usage scenarios could cause edits in the browser to not be reflected in the host. The lingering edge cases have been addressed to ensure edits always arrive.
- **On-Premises and Self-Signed Certs**  
  Organizations using an internal certificate authority can configure CodeTogether to automatically accept the certificate simplifying deployment.
- **Key Bug Fixes**  
  Small but beneficial fixes land to ensure reliable editing in a wide array of editor types!

## [2.1.0] - 2020.8.6
- **Syntax Coloring for Cobol, Dart, and Elixir**  
  Language coloring and completion aides have been added for Cobol, Dart, and Elixir.
- **.codetogether.ignore Allows Hiding Files/Folders**  
  Files or Folders that should not be available in the session can be hidden by creating .codetogether.ignore files in the root of projects using .gitignore like glob patterns.
- **Preview: File Uploads from Browser**  
  Files can be added to the shared project simply by dragging them into the Explorer in the browser.
- **IntelliJ Fixes for Code Alone**  
  In certain scenarios, edits made from the browser would not show up in IntelliJ and related IDEs. This has been rectified.
- **Various General Fixes**  
  Numerous fixes reported including navigation reliability, and exposing Toggle Word Wrap have been addressed.

## [2.0.1] - 2020.7.16
- **Little Fixes Land**  
  In VS Code, certain folders may not have loaded right in the browser. In IntelliJ, editing in markdown files could fail from the browser side. Both are fixed including a couple other small tweaks.
- **On-Premises Base Image**  
  The Docker image used for On-Premises has been migrated to a RedHat UBI base.

## [2.0.0] - 2020.7.6
- **2.0 Has Arrived!**  
  Packed with new features, 2.0 brings an all new experience to remote development!
- **Simultaneous Editing**  
  Highly requested support for editing in multiple files by different people is now available! Even coding in the same file is smoothed out with seamless control change.
- **CodeTogether or Alone**  
  Now you can easily split off from the group to explore or code independently. Working together? Selection is now naturally shared across collaborators.
- **IDE Themes and Key Bindings**  
  Choose to code with your favorite key bindings and IDE looks from IntelliJ, Eclipse and VS Code, regardless of what IDE is being used.
- **On-Premises Ready**  
  Looking for more security? CodeTogether can be deployed behind the firewall for even greater control over source exposure.
- **Quick Fix Support**  
  Building on the new 2.0 base, it is now possible to use Quick Fixes right from the browser using full IDE smarts. More IDE aids are coming!
- **Oodles of Fixes**  
  Dozens of other fixes have landed in this release, from compatibility with more IDEs to coding reliability, and syntax coloring for Twig, Scala and more!

## [1.2.0] - 2020.5.21
- **End-to-End Encryption**  
  All sessions now include full end-to-end encryption! Beyond secure SSL connections between endpoints, end-to-end AES encryption ensures that your source is never exposed, even if our secure servers were somehow exploited.
- **Anonymous Usage**  
  Now you can use CodeTogether sessions without logging in or registering. As CodeTogether is free for all, no need to require logins!
- **Tab Sizes and Spaces**  
  CodeTogether automatically detects tab sizes and space-usage to ensure that while coding in the browser, you always get a consistent and expected experience.
- **IntelliJ Robustness**  
  Jetbrains IDEs support picks up numerous fixes from support for multiple windows, to consistent marker relaying, and improvements in content assist. Thanks for all the reports!
- **Running Behind Proxies**  
  Sessions would sometimes not start correctly when running behind proxies in both Eclipse and IntelliJ. Both hosts have been fixed to work right.
- **Transparency on GitHub**  
  All CodeTogether issues and resolution are now tracked on GitHub Issues. Check out the milestones to see what else was fixed for this release and more.

## [1.1.0] - 2020.4.29
- **Now Available for IntelliJ**  
  CodeTogether is now in early access for IntelliJ! In addition, CodeTogether has been taken out of early access for Eclipse and VS Code. Thanks for all the great feedback!
- **Presence Visualization**  
  Participants and hosts alike can see rich visualization of what others in the session are up to including seeing who is browsing code on their own, recent edit locations and more.
- **Seamlessly Take Control**  
  Participants can now take control by typing. If enabled, typing can be immediate with no dialog or confirmation allowing rapid control changes when working together.
- **Editing Reliability**  
  Numerous fixes have been implemented to ensure reliable coding, from oddities with non-foreground browser windows to timing issues when typing fast.
- **Format Files and Language Smarts**  
  Participants can now choose to remotely format files, using formatting configuration on the host. Language smarts have also been enhanced for multiple Eclipse editors giving better content assist and as-you-type marker validation.
- **Reliability of Content Assistance**  
  When using code completion, characters could get lost if it took a while to complete the content assist action. In addition, key trigger characters are now relayed to the browser making coding more natural.

## [1.0.5] - 2020.4.8
- **Improved Control Visualization**  
  Editors now show who is in control both on the host side and in the browser.
- **Browser-side Light and Dark Themes**  
  Participants can now choose to code in a light or dark theme when working in CodeTogether sessions.
- **Control and Follow Keybindings in Browser**  
  Key bindings now allow changing Control or Follow: use CMD/CTRL-K then C for control, CMD/CTRL-K then F for follow.
- **Update Details**  
  When starting a session, if an optional client update is available, details about the update will be provided.
- **Numerous Fixes**  
  Various other improves have landed including correctly relaying intra-line selection, and more editing consistency.

## [1.0.4] - 2020.3.27
- **Improved Searching**  
  Searching in the workspace now gives consistent results when retriggering searching.
- **Create Files from Browser**  
  Correctly allow new files to be created from the browser.
- **Fixes for Control Changes**  
  Improve consistency when multiple participants take turns controlling.

## [1.0.3] - 2020.3.18
- **Participant Names**  
  Participants can now specify names from the browser when joining sessions.
- **Improves Integrity Checks**  
  When relaying and processing changes, additional integrity checks have been added to ensure editing consistency.

## [1.0.2] - 2020.3.6
- **Fixes Copy/Paste of Session on Linux**  
  Copying the session URL was not working as expected and the library has been changed.

## [1.0.1] - 2020.3.5
- **CodeTogether is Public!**  
  We are happy to announce CodeTogether being generally available and no longer in private trials!
