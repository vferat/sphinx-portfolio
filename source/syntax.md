---
orphan: true
---

# Syntax

Here is a brief overview of syntax that can be use to populate this website.

Please check the [markdown guide](https://www.markdownguide.org/basic-syntax/)
to learn the basic ``markdown`` syntax.

More details on the website configuration can be found on the [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/) website
and the  [sphinx-design](https://sphinx-design.readthedocs.io/en/pydata-theme/index.html) website.

- Grids: https://sphinx-design.readthedocs.io/en/pydata-theme/grids.html
- Cards: https://sphinx-design.readthedocs.io/en/pydata-theme/cards.html
- Dropdowns: https://sphinx-design.readthedocs.io/en/pydata-theme/dropdowns.html
- Tabs: https://sphinx-design.readthedocs.io/en/pydata-theme/tabs.html
- Badges: https://sphinx-design.readthedocs.io/en/pydata-theme/tabs.html
- Buttons: https://sphinx-design.readthedocs.io/en/pydata-theme/tabs.html
- Icons: https://sphinx-design.readthedocs.io/en/pydata-theme/tabs.html
- Code blocks: https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/theme-elements.html#code-blocks
- Inline code: https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/theme-elements.html#code-blocks
- Admonition sidebars: https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/theme-elements.html#admonition-sidebars


## Figures

``````restructuredtext
```{figure} _static/images/image_01.png
---
width: 60%
alt: My figure text
name: my_figure
---
And here is my figure caption.
```
``````

```{figure} _static/images/image_01.png
---
width: 60%
alt: My figure alternative text
name: my-figure
---
And here is my figure caption.
```

You can use the `:name:` variable to link to figure:
``````restructuredtext
{ref}`my-figure`
``````
link to the figure {ref}`my-figure`


## Mathematics
``````restructuredtext
```{math}
:label: eq-label

z=\sqrt{x^2+y^2}
```
``````

```{math}
:label: eq-label

z=\sqrt{x^2+y^2}
```

You can use the `label` variable to link to equation:
``````restructuredtext
{eq}`eq-label`
``````
link to the equation {eq}`eq-label`


## Notes
````
```{note}
A note
```
````

```{note}
A note
```


## References and bibliographies

### References

The extension `sphinxcontrib-bibtex` allows to manage the bibliography of this site.
To cite an article, add the reference in bibtex format to the `bibliography.bib` file and
refer to the citation using the bibtex keyword:

````markdown
{footcite}`ardhana2023imagined`
````

Will be rendered as {footcite}`ardhana2023imagined`

### Bibliography

To insert a bibliography on the page use

````markdown
```{footbibliography}
```
````

```{footbibliography}
```


## Custom

You can add HTML content directly in your `markdown` files:


``````html

<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/3TOCzZr8KJzPEmenbBLGT5?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

``````

<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/3TOCzZr8KJzPEmenbBLGT5?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

## Toggle content with buttons


The extension `sphinx_togglebutton` allows to add content in toggle frames.

``````restructuredtext

```{image} https://media1.tenor.com/m/ELIEPKi7qIYAAAAd/disco-elysium-rave.gif
:class: toggle
```

``````

```{image} https://media1.tenor.com/m/ELIEPKi7qIYAAAAd/disco-elysium-rave.gif
:class: toggle
```