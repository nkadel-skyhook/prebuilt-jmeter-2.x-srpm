prebuild-jmeter-2.x-srpm packing for jmeter SRPM
================================================

This is a quick and dirty wrapper to bundle the Apache Jmeter
software into a workable RPM for RHEL 6 deployment

License
-------

Apache 2.0, available at http://www.apache.org/licenses/


Build
-----

* Build with "mock" on all tested platforms by running "make"
* For local environment compilaition, use "make build"

Usage
-----

The RPM adds an /etc/profile.d/jmeter.sh to enable a PATH for
jmeter. Simply install this package, log in the local host as a normal
user, and type "jmeter".

Author
------

Nico Kadel-Garcia <nkadel@shykookwireless.com>
