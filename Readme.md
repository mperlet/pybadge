# pybadge ![pylint Score](http://www.mperlet.de/pybadge/badges/5.00.svg)

pylint badges for everyone!

## Howto

1. Check your pylint score with `pylint` or `python3-pylint`
2. Goto: http://www.mperlet.de/pybadge/ and insert your score
3. Copy the generated markdown link into your README

## Color intervals

`if score < 3.0:`
    ![pylint Score](http://www.mperlet.de/pybadge/badges/2.99.svg)
`elif score >= 3.0 and score < 7.0:`
    ![pylint Score](http://www.mperlet.de/pybadge/badges/5.51.svg)
`else:`
    ![pylint Score](http://www.mperlet.de/pybadge/badges/9.73.svg)

## Limitations

* negative scores are not supported
* no dynamic badges, needs something like continuous integration services

## Idea

I was looking for python badges and could not find any for pylint.
The idea for this implementation is inspired from the blogpost
http://www.desmondrivet.com/blog/technical/pylint-badges.html.
