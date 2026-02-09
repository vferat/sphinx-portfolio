# sphinx-portfolio


## Setup


### Use this template


(Click here) [https://github.com/new?template_name=sphinx-portfolio&template_owner=vferat] or on the `use this template` button on top of the repository page to create your own portfolio.

If you want the website to be hosted on `https://{gh_username}.github.io/` name the repository:
`{gh_username}.github.io` where `{gh_username}` is you github username.

### Github pages

Go to your repository settings -> pages -> Select "Deploy from a branch" for "Build and deployment". Select the `gh-pages` branch.
If the `gh-pages` branch does not exist yet, you can create it from the github website.

### Github actions

Go to your repository settings -> actions -> Workflow permissions: select Read and write permissions.

You can also enable 
Allow GitHub Actions to create and approve pull requests

## Customization

### Edit configuration

Edit the `source/conf.py` file.

### Profile


### favicon

### description


### Style

Edit `source/_static/custom.css`

### Navbar

#### Pages

Create a new markdown (`.md`) file in the root folder of the documentation (`./source`).
Add the filename (without the extension) to the toctree section of `source\index.md`

``````
```{toctree}
:maxdepth: 2
:hidden:
about
publications
syntax
```
``````

#### Socials media links

In `conf.py`, edit the `"icon_links"` entry.


### Bibliography

#### Populate bibliography

google scholar -> cite -> bibtex -> copy / paste
Add the ressource to the `./source/ibliography.bib` file.

#### Reference

In any page of the website, use the foloow to make a reference.

```markdown
{footcite}`reference_name`
```

And don't forget to add the bibliography at the end of the page:

````markdown
```{footbibliography}
```
````