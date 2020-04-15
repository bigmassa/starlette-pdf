
[![Sourcery](https://img.shields.io/badge/Sourcery-refactored-blueviolet.svg)](https://sourcery.ai)
![](https://github.com/accent-starlette/starlette-pdf/workflows/Testing%20Workflow/badge.svg?branch=master)
![](https://codecov.io/gh/accent-starlette/starlette-pdf/branch/master/graph/badge.svg)
![](https://github.com/accent-starlette/starlette-pdf/workflows/Deploy%20to%20Amazon%20ECR/badge.svg)

## Page rule CSS

- https://www.quackit.com/css/at-rules/css_top-center_at-rule.cfm

## Example html

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Lorem ipsum</title>
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,700" rel="stylesheet">
        <style>
            @page {
                @top-left {
                    font-family: 'Open Sans';
                    background: #bed600;
                    content: counter(page);
                    height: 1cm;
                    text-align: center;
                    width: 1cm;
                }
                @top-center {
                    background: #bed600;
                    content: '';
                    display: block;
                    height: .05cm;
                    opacity: .5;
                    width: 100%;
                }
                @top-right {
                    font-family: 'Open Sans';
                    content: string(heading);
                    font-size: 9pt;
                    height: 1cm;
                    vertical-align: middle;
                    width: 100%;
                }
            }
            @page :first {
                background-color: #bed600;
                margin: 0;
            }
            @page :blank {
                @top-left {
                    background: none;
                    content: '';
                }
                @top-center {
                    content: none;
                }
                @top-right {
                    content: none;
                }
            }
            @page no-chapter {
                @top-left {
                    background: none;
                    content: none;
                }
                @top-center {
                    content: none;
                }
                @top-right {
                    content: none;
                }
            }
            html {
                color: #393939;
                font-family: 'Open Sans';
                font-size: 11pt;
                font-weight: 300;
                line-height: 1.5;
            }
            h1, h2 {
                font-family: 'Open Sans';
                font-weight: 400;
            }
            h1 {
                color: #ffffff;
                font-size: 38pt;
                margin: 5cm 2cm 0 2cm;
                width: 100%;
            }
            h2 {
                break-before: always;
                font-size: 28pt;
                padding-top: 1cm;
                string-set: heading content();
            }
            article#cover {
                align-content: space-between;
                display: flex;
                flex-wrap: wrap;
                height: 297mm;
            }
            article#cover footer {
                color: #bed600;
                background: #ffffff;
                flex: 1 50%;
                margin: 0 -1cm;
                padding: 1cm 0 1.3cm 2.7cm;
                white-space: pre-wrap;
            }
            article#toc {
                break-before: right;
                break-after: left;
                page: no-chapter;
            }
            article#toc ul {
                list-style: none;
                padding-left: 0;
            }
            article#toc ul li {
                margin: .25cm 0;
                padding-top: .25cm;
            }
            article#toc ul li::before {
                color: #bed600;
                content: '• ';
                font-size: 40pt;
                line-height: 16pt;
                vertical-align: bottom;
            }
            article#toc ul li a {
                color: inherit;
                text-decoration: inherit;
            }
            article#toc ul li a::before {
                content: target-text(attr(href));
            }
            article#toc ul li a::after {
                color: #bed600;
                content: target-counter(attr(href), page);
                float: right;
            }
        </style>
    </head>
    <body>
        <article id="cover">
            <h1>Lorem Ipsum</h1>
            <footer>&copy; Accent Design Group Limited</footer>
        </article>
        <article id="toc">
            <h2>Table of contents</h2>
            <ul>
                <li><a href="#intro-title"></a></li>
            </ul>
        </article>
        <article id="intro">
            <h2 id="intro-title">Lorem ipsum dolor sit amet</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </article>
    </body>
</html>
```