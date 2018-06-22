psrv
====

Simple web utility to serve up a system's statistics using psutil.  This
can be referred to as ps service or process and service remote viewer.
This is a basic demo proof of concept that really aims to showcase how
Python backends and JavaScript frontends can be integrated together.

This demo may be installed using the following commands into a Python
virtual environment:

.. code::

    $ git clone https://github.com/metatoaster/psrv.git
    $ cd psrv
    $ pip install -e .[dev,webpack,scss]
    $ calmjs npm --install -i -D psrv[dev,webpack,scss]
    $ python setup.py build
    $ psrv-demo

Connect a web browser to http://localhost:8000 and a simple page showing
the current CPU and memory utilization for the current machine will be
visible with updates done by polling the status endpoint every three
seconds (defined in the JavaScript code in this module).
