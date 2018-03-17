# pybadge ![pylint Score](pylint.svg)

pylint badges for everyone!

## Howto

1. Run `pylint --output-format=json`
### bash alias for markdown text
run `pybadge <pyfile>`
```
function pybadge() {
	echo "![pylint Score](https://mperlet.github.io/pybadge/badges/$(pylint $1 2> /dev/null | tail -n2 | awk '{print $7}' | cut -d"/" -f1).svg)"
}
```
## Color intervals

0.00 < ![pylint Score](https://mperlet.github.io/pybadge/badges/1.50.svg) < 3.00 < ![pylint Score](https://mperlet.github.io/pybadge/badges/5.51.svg) < 7.00 ![pylint Score](https://mperlet.github.io/pybadge/badges/9.73.svg) < 10.00

## Limitations

* negative scores are not supported
* no dynamic badges, needs something like continuous integration services

## Idea

I was looking for python badges and could not find any for pylint.
The idea for this implementation is inspired from the blogpost
http://www.desmondrivet.com/blog/technical/pylint-badges.html.
