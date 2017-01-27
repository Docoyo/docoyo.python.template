# Python 3 package template

The package demonstrates how a python 3 package can be structured. In addition, 
it is already configured with the necessary Visual Studio Code launch, lint,
and format configurations.

The template uses:

* [yapf](https://github.com/google/yapf)
* [pylint](https://www.pylint.org)

The configuration of yapf (.style.yapf) is set to google with two-space indent. It matches the google style conventions defined in .pylintrc. They are taken from <https://github.com/vinitkumar/googlecl/blob/master/googlecl-pylint.rc> and slightly modified to allow two-character variables and function arguments.


## Recommendations

### Use the launch configuration "Python test" to debug tests

The build-in test discovery of the python module is quite flaky at this time. Opposed to that, the "Run all unit tests" functionality works quite well and the status message gives and indication of the stability. A good idea is to map a key to run all test, for instance as:

```json
{
  "key": "ctrl+alt+r",
  "command": "python.runtests"
}
```

# Authors
[Nicolaj Kirchhof](https://github.com/nicolajkirchhof)

---
[docoyo 2017](www.docoyo.com)

# License
MIT License

Copyright (c) 2017 docoyo 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
