# skf-editor [GSOC'21]

### What is SKF?
Security Knowledge Framework (SKF) is a tool that is used as a guide for building and verifying secure software. It can also be used to train developers about application security. The OWASP Security Knowledge Framework is an expert system web-application that uses the OWASP Application Security Verification Standard and other resources. It can be used to support developers in pre-development (security by design) as well as after code is released (OWASP ASVS Level 1-3).

## What is skf-editor?
SKF-editor is a browser-based text editor. It allows the user to visualize the source code of the current lab and interactively play with a sandbox environment that allows for code fixing and testing. The users are provided with the ability to not only exploit the vulnerability vias SKF labs, embedded in a browser-like component alongside the editor, but visualize the underlying source of the security issue and attempt to fix it. 

This fixing feature verifies the user solution for inconsistencies in syntax, and after proving that the service won’t be crashed by the changes, run the newly modified version overriding the original one. In this way we enable the user to dynamically test for the secure code fragment that fixes the root cause of the issue exemplified in the lab.


## Main components

### Browser
### File explorer
### Code editor
### Terminal


# TODO
This humble contribution to open source is not near to perfect and still needs enhancements that I as contributor expect to accomplish outside GSoC21. We encourage the open source community to flag any missing feature or enhancement so we can build the best version of this contribution. The known open issues are:

* Make panels resizable
* Implement logs module to centralize all application and container logs to improve debugging experience
* Implement backup feature to have file diffing and versioning in the frontend
* Add feature for code linting/checking to validate the user solution
* Implement abuse test cases to enhance the code-fixing by presenting the user with the automated test suite for bypasses for the provided solution



