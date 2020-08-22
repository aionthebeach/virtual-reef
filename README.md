# Virtual Reef

## Maintainers
Owen Pierce (owen@aionthebeach.com)  
Praful Mathur (praful@aionthebeach.com)  
Eric Simmons (eric@aionthebeach.com)


## Goals
Reef Check needs a good way to generate visualizations based on the data from surveys.
The intended audience is people who may not be familiar with the underwater environment,
so granular precision isn't as important as giving an accurate impression of the environment
over time.

Virtual Reef is a tool to build images of the coastal reefs surveyed by California Reef Check.
We want to generate images that show the density of plants, fish, and invertebrates on the reef. 
We will read in the survey data for each 

## Installation
1. Install [Python 3.8](https://www.python.org/downloads/). Any 3.8 version should be fine.
2. Install [pipenv](https://github.com/pypa/pipenv) by running `pip install pipenv`
3. Configure pipenv to use Python 3 by running `pipenv --three`
4. Install Django `pipenv install django`
5. Activate your pipenv shell by running `pipenv shell`. You will need to have the pipenv shell active to run the server.

## Running the Project
In the `virtualreef` directory run `python manage.py runserver`

To see all Django commands run `python manage.py help`. The most common commands to run include:
* migrate
* makemigrations
* test

## How to Contribute
1. Go to our [Issues](https://github.com/aionthebeach/virtual-reef/issues) and add a comment asking to work on an unassigned issue. Feel free to ask questions about how to solve an issue! We try to provide as much detail as possible about an issue to solve it, but details can come up while working on something that the creator of the issue didn't think about.
2. Fork the project to get a copy you can work on freely.
3. Make your changes on your forked copy (edit code, edit assets, etc).
4. Create a Pull Request to [the main repo](https://github.com/aionthebeach/virtual-reef)
5. Contact a maintainer to review your PR
6. After review, your PR is either **Accepted** and will be merged, or will have **Changes Requested**. The requested changes should be detailed in comments from a maintainer.

## FAQs
### My server doesn't run when I try `python manage.py runserver`
Did you get an error like this?
`ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?`
If so, make sure you ran `pipenv install django` and `pipenv shell`

If you got another kind of error, contact the maintainers and we'll do our best to help!

### Where does the data live?
We keep our data in [Quilt](https://open.quiltdata.com/b/ai-on-the-beach/tree/aionthebeach/reef-check/).

## License
This project uses the [Apache License](https://github.com/aionthebeach/virtual-reef/blob/main/license.txt).
