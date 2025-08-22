# Plotly DASH - Multi-Page Project Structure

Many online examples for DASH dashboards are presented in a single file, and although this is
fine for small simple dashboards, it becomes impossible to manage as a project increases in size,
and potentially onto multiple pages.

It therefore becomes necessary to start breaking up the single file to create a logical project 
structure to make project management easier.

However, there are limited examples available on how to acheive a structured multi-page app, and 
there appears to be no standard "official" way to go about this. Furthermore, any examples of 
mulipage apps present a bear-bones structure that typically doesn't include any example graphing 
etc. leaving some guesswork with regard to actually getting the app to work reliably.

## Aim

With the above in mind, this repo is primarily concerned with three items in relation to creating
a DASH dashboard:

1. Multi-page
2. Logical project structure (i.e. not all in one file)
3. Fully functional with data and graphing

## Other features

As mentioned above, a lot of examples are limited in terms of what they include. They typically 
only provide information on the EXACT thing they are referring to rather than having 
a fully functional example with data etc.

Although, this is understandable to a certain extent, as too much information can be confusing, 
sometimes it can leave the user with a lot to figure out later down the line.

This repo therefore provides a fully functional base that the user can run, and experiment with,
straight away, and therefore use a reference point to develop their owen project from.

This repo includes the following, in addition to being multipage and featuring a logical structure
of folders and files:

1. A sidebar which lists the available pages, and highlights which one is active as you change page
2. A header with website name, logo and dark/light theme switch
3. Mobile ready (i.e. responsive layout) with collapsible sidebar
4. Dark/light theme switching, including the Plotly graphs that are included
5. Two different API integrations, one local (Plotly Gapminder), and one remote with logic for API keys etc. (NinjasAPI) 
6. Git ready, with logic to keep API keys out of the code, and auto DEBUG/production mode (python-dotenv)
7. A simple example of styling using style.css
8. Utilises DASH Mantine Components for styling

## References

[Plotly DASH](https://dash.plotly.com/)
[DASH Mantine Components](https://www.dash-mantine-components.com/)

## License

The content of this project is licensed under the [MIT License](LICENSE.md)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z7G2C89)




