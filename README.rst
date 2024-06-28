==================================
PostgreSQL Performance Farm Worker
==================================

These are instructions on setting up your worker for the `PostgreSQL
Performance Farm <https://github.com/PGPerfFarm/pgperffarm-buildbot>`_. The
worker is a `Buildbot <https://buildbot.net/>`_ worker that needs to be
configured and setup for the PostgreSQL Performance Farm.

------------
Installation
------------

The worker does its thing primarily in its own directory.  Thus it is
currently limited to using only the storage it is residing on.

In addition to installing the files in this repository, additional software may
be needed for each of the following tests.  See the following section for each
test that this worker intends to run for more details.

DBT-2
-----

DBT-2 is a fair-use implementation of the TPC Benchmark(TM) C.  No additional
files are need to run this test.

DBT-3
-----

DBT-3 is a fair-use implementation of the TPC Benchmark(TM) H.  The TPC-H Tools
must be downloaded by you or your organization.  Create a subdirectory `dbgen`
at the top level this repository and unzip the tools into that subdirectory.
Follow the section `Building TPC-H Tools
<https://github.com/osdldbt/dbt3/blob/main/doc/dbt3.rst#building-tpc-h-tools>`_
on how to download compile the tools.

DBT-5
-----

DBT-5 is a fair-use implementation of the TPC Benchmark(TM) E.  The TPC-E Tools
must be downloaded by you or your organization.  Create a subdirectory `egen`
at the top level this repository and unzip the tools into that subdirectory.
Follow the section `Building TPC-E Tools
<https://github.com/osdldbt/dbt5/blob/main/doc/user-guide.rst>`_ on how to
download compile the tools.

DBT-7
-----

DBT-7 is a fair-use implementation of the TPC Benchmark(TM) DS.  The TPC-DS
Tools must be downloaded by you or your organization.  Create a subdirectory
`dsgen` at the top level this repository and unzip the tools into that
subdirectory. Follow the section `Building TPC-DS Tools
<https://github.com/osdldbt/dbt7/blob/main/doc/dbt7.rst#building-tpc-ds-tools>`_
on how to download compile the tools.

-------------
Configuration
-------------

Identify yourself
-----------------

Put your name and email address into the `info/admin` file.

Identify the server
-------------------

Put a description of the server into the `info/host` file.  An example of what
to put is coming...

Create `settings.py`
--------------------

Copy `settings.py.sample` to `settings.py` and update the *WORKERNAME* and
*SECRET* accordingly.
