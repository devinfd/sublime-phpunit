<h1 align="center">PHPUnit Kit</h1>

<p align="center">
    <a href="https://github.com/gerardroche/sublime-phpunit/actions/workflows/ci.yml"><img alt="GitHub CI Status" src="https://github.com/gerardroche/sublime-phpunit/actions/workflows/ci.yml/badge.svg?branch=master"></a>
    <a href="https://ci.appveyor.com/project/gerardroche/sublime-phpunit/branch/master"><img alt="AppVeyor CI Status" src="https://ci.appveyor.com/api/projects/status/wknvpma8qgjlqh1q/branch/master?svg=true"></a>
    <a href="https://codecov.io/gh/gerardroche/sublime-phpunit"><img src="https://codecov.io/gh/gerardroche/sublime-phpunit/branch/master/graph/badge.svg?token=rnB0MiBXlK" alt="CodeCov Coverage Status" /></a>
    <a href="https://packagecontrol.io/packages/PHPUnitKit"><img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/PHPUnitKit.svg"></a>
</p>

PHPUnit support for [Sublime Text](https://sublimetext.com).

<img src="https://raw.githubusercontent.com/gerardroche/sublime-phpunit/master/screenshot.png" width="585" alt="PHPUnitKit">

## Features

* Run a test method
* Run a test file
* Run the test suite
* Run the nearest test
* Run the last test
* Run multiple test methods using a multiple cursor
* Auto run test on save
* Colour output
* Fast jump to next and previous failure
* Fast switch between test and file-under-test
* Toggle CLI options from the command palette
* Fully customized CLI options configuration
* Support for
    - [Artisan] - Artisan is the command line interface included with Laravel.
    - [Composer] - Composer is a Dependency Manager for PHP.
    - [iTerm2] - iTerm2 brings the terminal into the modern age.
    - [Kitty] - Kitt is a fast, feature-rich, cross-platform, GPU based terminal.
    - [ParaTest] - ParaTest adds parallel testing support in PHPUnit.
    - [Pest] - Pest is a testing framework with a focus on simplicity.
    - [xterm] - A terminal emulator for the X Window System.
- Zero configuration required

Read [Running PHPUnit Tests from Sublime Text](https://blog.gerardroche.com/2023/05/05/running-phpunit-tests-within-sublime-text/) for a quick introduction.

## Installation

Install [PHPUnitKit](https://packagecontrol.io/packages/PHPUnitKit) via Package Control.

## Setup

Zero configuration required.

Optional. Add your preferred key bindings.

Menu → Preferences → Key Bindings

```js
{ "keys": ["ctrl+shift+a"], "command": "phpunit_test_suite" },
{ "keys": ["ctrl+shift+c"], "command": "phpunit_test_cancel" },
{ "keys": ["ctrl+shift+f"], "command": "phpunit_test_file" },
{ "keys": ["ctrl+shift+l"], "command": "phpunit_test_last" },
{ "keys": ["ctrl+shift+n"], "command": "phpunit_test_nearest" },
{ "keys": ["ctrl+shift+r"], "command": "phpunit_test_results" },
{ "keys": ["ctrl+shift+s"], "command": "phpunit_test_switch" },
{ "keys": ["ctrl+shift+v"], "command": "phpunit_test_visit" },
```

## Commands

Command                              | Description
:------                              | :----------
**PHPUnit:&nbsp;Test&nbsp;Nearest**  | In a test file runs the test nearest to the cursor, otherwise runs the test for the current file.
**PHPUnit:&nbsp;Test&nbsp;File**     | In a test file runs all tests in the current file, otherwise runs test for the current file.
**PHPUnit:&nbsp;Test&nbsp;Suite**    | Runs the whole test suite.
**PHPUnit:&nbsp;Test&nbsp;Last**     | Runs the last test.
**PHPUnit:&nbsp;Test&nbsp;Switch**   | In a test file opens the file under test, otherwise opens the test file.
**PHPUnit:&nbsp;Test&nbsp;Visit**    | Visits the test file from which you last run your tests (useful when you're trying to make a test pass, and you dive deep into application code and close your test buffer to make more space, and once you've made it pass you want to go back to the test file to write more tests).
**PHPUnit:&nbsp;Test&nbsp;Results**  | Opens the exec test output panel.
**PHPUnit:&nbsp;Test&nbsp;Cancel**   | Cancels any currently running test.
**PHPUnit:&nbsp;Test&nbsp;Coverage** | Opens code coverage in browser.
**PHPUnit:&nbsp;Toggle...**             | Toggle PHPUnit options.

## Key Bindings

Key         | Description
:---        | :----------
`F4`        | Jump to next failure
`Shift+F4`  | Jump to previous failure

## Strategies

PHPUnitKit can run tests using different execution environments called "strategies". To use a specific strategy, assign it to a setting:

```js
"phpunit.strategy": "kitty"
```

| Strategy              | Identifier    | Description
| :------:              | :--------:    | :----------
| **Basic** (default)   | `basic`       | Sends test commands to Sublime Text exec output panel.
| **iTerm2.app**        | `iterm`       | Sends test commands to `iTerm2 >= 2.9` (useful in MacVim GUI).
| **[Kitty]**           | `kitty`       | Sends test commands to Kitty terminal.
| **[xterm]**           | `xterm`       | Sends test commands to xterm terminal.

## Configuring

Menu → Preferences → Settings

| Setting                   | Type               | Default          | Description
| :------------------------ | :----------------- | :--------------- | :----------
| `phpunit.executable`      | `string` or `list` | Auto discovered. | Path to PHPUnit executable.
| `phpunit.php_executable`  | `string`           | Auto discovered. | Path to PHP executable.
| `phpunit.options`         | `dict`             | `{}`             | CLI Options to pass to PHPUnit.
| `phpunit.save_all_on_run` | `boolean`          | `true`           | Save all dirty buffers before running tests.
| `phpunit.on_post_save`    | `list`             | `[]`             | Auto commands when views are saved.
| `phpunit.prepend_cmd`     | `list`             | `[]`             | Prepends test runner command.
| `phpunit.strategy`        | `string`           | `basic`          | Execution environment to run tests.
| `phpunit.composer`        | `boolean`          | `true`           | Use Composer installed executables, if they exist.
| `phpunit.artisan`         | `boolean`          | `false`          | Use Artisan to run tests, if it exists.
| `phpunit.paratest`        | `boolean`          | `false`          | Use ParaTest to run tests, if it exists.
| `phpunit.pest`            | `boolean`          | `false`          | Use Pest to run tests, if it exists.
| `phpunit.font_size`       | `integer`          | Editor default.  | Font size of PHPUnit output.
| `phpunit.debug`           | `boolean`          | `false`          | Prints test runner debug information.

### CLI Options

If you want some CLI options to stick around, you can configure them in your settings.

Menu → Preferences → Settings

```json
{
    "phpunit.options": {
        "no-coverage": true,
        "no-progress": true,
        "colors=never": true,
        "order-by=": "defects",
        "coverage-html": "build/coverage",
        "d": ["display_errors=1", "xdebug.scream=0"],
    }
}
```

The above options will be passed to PHPUnit as CLI options:

```shell
-d "display_errors=1" \
-d "xdebug.scream=0" \
--no-coverage \
--no-progress \
--colors=never \
--order-by=defects \
--coverage-html build/coverage
```

**Example:** Ignore code coverage reporting configured in the XML configuration file

This can help keep your tests fast. You can toggle no-coverage from the command palette when you need it.

Menu → Preferences → Settings

```json
{
    "phpunit.options": {
        "no-coverage": true,
    }
}
```

**Example:** Stop after first error, failure, warning, or risky test

Menu → Preferences → Settings

```json
{
    "phpunit.options": {
        "stop-on-defect": true
    }
}
```

**Example:** Disable progress and output

This is useful if you are migrating from PHPUnit to Pest and want to hide superfluous output.

Menu → Preferences → Settings

```json
{
    "phpunit.options": {
        "no-progress": true,
        "no-output": true,
    }
}
```

### PHPUnit Executable

The path to the PHPUnit executable to use when running tests. Environment variables and user home directory ~ placeholder are expanded. The executable can be a string or a list of parameters.

Default: Auto discovery.

**Examples**

Menu → Preferences → Settings

```json
{
    "phpunit.executable": "vendor/bin/phpunit",
    "phpunit.executable": "~/path/to/phpunit",
    "phpunit.executable": ["artisan", "test"]
}
```

### PHP Executable

The path to the PHP executable to use when running tests. Environment variables and user home directory ~ placeholder are expanded.

Default: Auto discovery.

**Examples**


Menu → Preferences → Settings

```json
{
    "phpunit.php_executable": "~/.phpenv/versions/8.2/bin/php"
}
```

### Prepend cmd

You can prepend the runner command with a list of additional parameters.

**Example:** Run tests in your preferred terminal

```json
{
    "phpunit.prepend_cmd": [
         "/usr/bin/terminal",
         "--hold"
    ]
}
```

### Auto Commands

You can configure the `on_post_save` event to run the "Test File" command when views are saved. This will instruct the runner to automatically run a test every time it is saved.

**Example:** Run Test File on Save

Menu → Preferences → Settings

```json
{
    "phpunit.on_post_save": [
        "phpunit_test_file"
    ]
}
```

### Toggle Commands

You can toggle many PHPUnit CLI options from the command palette.

Command Palette → PHPUnit: Toggle ...

#### Execution

| Caption                                         | Description
| :---------------------------------------------- | -----------------------------
| PHPUnit: Toggle --process-isolation | Run each test in a separate PHP process
| PHPUnit: Toggle --globals-backup | Backup and restore `$GLOBALS` for each test
| PHPUnit: Toggle --static-backup | Backup and restore static properties for each test
| PHPUnit: Toggle --strict-coverage | Be strict about code coverage metadata
| PHPUnit: Toggle --strict-global-state | Be strict about changes to global state
| PHPUnit: Toggle --disallow-test-output | Be strict about output during tests
| PHPUnit: Toggle --enforce-time-limit | Enforce time limit based on test size
| PHPUnit: Toggle --dont-report-useless-tests | Do not report tests that do not test anything
| PHPUnit: Toggle --stop-on-defect | Stop after first error, failure, warning, or risky test
| PHPUnit: Toggle --stop-on-error | Stop after first error
| PHPUnit: Toggle --stop-on-failure | Stop after first failure
| PHPUnit: Toggle --stop-on-warning | Stop after first warning
| PHPUnit: Toggle --stop-on-risky | Stop after first risky test
| PHPUnit: Toggle --stop-on-deprecation | Stop after first test that triggered a deprecation
| PHPUnit: Toggle --stop-on-notice | Stop after first test that triggered a notice
| PHPUnit: Toggle --stop-on-skipped | Stop after first skipped test
| PHPUnit: Toggle --stop-on-incomplete | Stop after first incomplete test
| PHPUnit: Toggle --fail-on-warning | Signal failure using shell exit code when a warning was triggered
| PHPUnit: Toggle --fail-on-risky | Signal failure using shell exit code when a test was considered risky
| PHPUnit: Toggle --fail-on-deprecation | Signal failure using shell exit code when a deprecation was triggered
| PHPUnit: Toggle --fail-on-notice | Signal failure using shell exit code when a notice was triggered
| PHPUnit: Toggle --fail-on-skipped | Signal failure using shell exit code when a test was skipped
| PHPUnit: Toggle --fail-on-incomplete | Signal failure using shell exit code when a test was marked incomplete
| PHPUnit: Toggle --cache-result | Write test results to cache file
| PHPUnit: Toggle --do-not-cache-result | Do not write test results to cache file
| PHPUnit: Toggle --order-by=default | Run tests in order: default
| PHPUnit: Toggle --order-by=defects | Run tests in order: defects
| PHPUnit: Toggle --order-by=depends | Run tests in order: depends
| PHPUnit: Toggle --order-by=duration | Run tests in order: duration
| PHPUnit: Toggle --order-by=no-depends | Run tests in order: no-depends
| PHPUnit: Toggle --order-by=random | Run tests in order: random
| PHPUnit: Toggle --order-by=reverse | Run tests in order: reverse
| PHPUnit: Toggle --order-by=size | Run tests in order: size

#### Reporting

| Caption                                         | Description
| :---------------------------------------------- | -----------------------------
| PHPUnit: Toggle --no-progress | Disable output of test execution progress
| PHPUnit: Toggle --no-results | Disable output of test results
| PHPUnit: Toggle --no-output | Disable all output
| PHPUnit: Toggle --display-incomplete | Display details for incomplete tests
| PHPUnit: Toggle --display-skipped | Display details for skipped tests
| PHPUnit: Toggle --display-deprecations | Display details for deprecations triggered by tests
| PHPUnit: Toggle --display-errors | Display details for errors triggered by tests
| PHPUnit: Toggle --display-notices | Display details for notices triggered by tests
| PHPUnit: Toggle --display-warnings | Display details for warnings triggered by tests
| PHPUnit: Toggle --reverse-list | Print defects in reverse order
| PHPUnit: Toggle --teamcity | Replace default progress and result output with TeamCity format
| PHPUnit: Toggle --testdox | Replace default result output with TestDox format

#### Logging

| Caption                                         | Description
| :---------------------------------------------- | -----------------------------
| PHPUnit: Toggle --no-logging | Ignore logging configured in the XML configuration file

#### Code Coverage

| Caption                                         | Description
| :---------------------------------------------- | -----------------------------
| PHPUnit: Toggle --path-coverage | Report path coverage in addition to line coverage
| PHPUnit: Toggle --disable-coverage-ignore | Disable metadata for ignoring code coverage
| PHPUnit: Toggle --no-coverage | Ignore code coverage reporting configured in the XML configuration file

### Custom Toggle Commands

You can create your own toggle commands.

The `phpunit_toggle_option` command accepts the following arguments:

Argument |  Type
:------- | :-----
`option` |  `string`
`value`  |  `boolean`, `string` (optional)

If `{value}` is not provided the option is assumed to be boolean.

**Example Commands**

Find your User directory via Menu → Browse Packages.

> User/Default.sublime-commands

```json
[
    {
        "caption": "PHPUnit: Toggle --no-coverage",
        "command": "phpunit_toggle_option",
        "args": {
            "option": "no-coverage"
        }
    },
    {
        "caption": "PHPUnit: Toggle --order-by=depends,defects",
        "command": "phpunit_toggle_option",
        "args": {
            "option": "order-by=",
            "value": "depends,defects"
        }
    }
]
```

**Example Key Binding**

Menu → Preferences → Key Bindings

```json
[
    {
        "keys": ["ctrl+n"],
        "command": "phpunit_toggle_option",
        "args": {
            "option": "no-coverage"
        }
    },
]
```

## NeoVintageous mappings

[NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) is a Vim emulator for Sublime Text.

Add your preferred mappings to your `.neovintageousrc` file.

**Example**

Command Palette → NeoVintageous: Open .neovinageousrc

```vim
nnoremap <leader>t :TestNearest<CR>
nnoremap <leader>T :TestFile<CR>
nnoremap <leader>a :TestSuite<CR>
nnoremap <leader>l :TestLast<CR>
nnoremap <leader>g :TestVisit<CR>
```

Don't forget to reload your .neovintageousrc file.

Command Palette → NeoVintageous: Reload .neovinageousrc

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Credits

Based initially on, and inspired by the awesome work of [maltize/sublime-text-2-ruby-tests](https://github.com/maltize/sublime-text-2-ruby-tests), [stuartherbert/sublime-phpunit](https://github.com/stuartherbert/sublime-phpunit), [janko-m/vim-test](https://github.com/janko-m/vim-test), and many others.

## License

Released under the [GPL-3.0-or-later License](LICENSE).

[Artisan]: https://laravel.com/docs/artisan
[Composer]: https://getcomposer.org
[Kitty]: https://github.com/kovidgoyal/kitty
[ParaTest]: https://github.com/paratestphp/paratest
[Pest]: https://pestphp.com
[iTerm2]: https://iterm2.com
[xterm]: https://invisible-island.net/xterm/
