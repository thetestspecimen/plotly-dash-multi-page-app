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

## Basic usage

To run the code in this repo follow the following steps:

### Create your virtual environment and install packages

Create your virtual environment and activate it. You can do this however you choose. For example:

```bash
cd project-folder
python -m venv venv
source venv/bin/activate
```

Then install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Create a ".env" file

The project uses ```python-dotenv``` to keep things like API Keys out of the project code by using a local file to store sensitive data, so you won't find this file included in the repo. You will need to create your own.

In the root of the project folder create a file with the name: ```.env```

As an example of what to include in the file, the following is what could be used in a local development environment:

```python
DEBUG = True
NINJAS_API_KEY = "s0L889BwIkT2ThjHDROVGH==fkluRlLyGgfUUPgh"
```

You would also have to get a legitimate API Key from NinjasAPI if you wanted to use that particular API.

Within a live environment you could change the ```DEBUG``` value to ```False```. Utilising this method has the advantage of being able to use git to update code between dev and live environments without having to change the ```DEBUG``` value every time, as this local file is not included in the git repo and is exclusive to the machine/server it is created on.

## Run the project

To run the project just execute the following line from within the project directory:

```python main.py```

You will then be told the local IP address that you can open in a browser to access the project front end.

## References

[Plotly DASH](https://dash.plotly.com/)

[DASH Mantine Components](https://www.dash-mantine-components.com/)

## License

The content of this project is licensed under the [MIT License](LICENSE.md)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z7G2C89)
