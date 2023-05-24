# Gratipay helps fund open source projects by providing a platform for weekly tips/donations. The current homepage lists all projects, along with images. Due to an ever-increasing number of projects, Gratipay is now hitting scaling problems! Help Gratipay design a solution such that only a handful of 'featured' projects are displayed on the homepage.

# At the heart of this solution, lies a single function:

# def get_featured_projects(all_projects):
#   ...
# all_projects is an array of projects, which are dictionaries/hashes of the format:

# {
#   'name': 'Project name',
#   'nreceiving_from': 10,
#   'receiving':  10,
# }
# get_featured_projects/getFeaturedProjects is expected to filter out a list of featured projects, based on the following specification:

# Always return 10 projects or less.
# Seven of the projects should be drawn randomly from a pool of the popular projects (a project with nreceiving_from > 5 is considered as popular). The remaining three should be taken randomly from amongst the rest.
# If there are less than 10 projects in total, just return all projects.
# If there are less than 7 popular projects, or less than 3 unpopular projects, fill the gaps from the other group of projects if possible.
# Randomize the order of results so that the popular projects don't always appear on top
# Note: Gratipay's codebase is open source, try to resist the temptation to cheat!

def get_featured_projects(all_projects):


    if len(all_projects) <=10:
        final_projects = all_projects
    else:

        counter = 0
        popular =[]
        unpopular =[]   
        for project in all_projects:
            #add id
            project['id'] = counter
            counter+=1
            #divide to popular and unpopular
            if project['nreceiving_from'] >5:
                popular.append(project)
            else:
                unpopular.append(project)
        try: 
            popular_sample = random.sample(popular, k=7)
            try:
                unpopular_sample =random.sample(unpopular, k=3)
            except ValueError:
                unpopular_sample = unpopular
                reserve_sample = []
                for x in popular:
                    if x not in popular_sample:
                        reserve_sample.append(x)
                additional_sample = random.sample(reserve_sample, k=(10-len(popular_sample)-len(unpopular_sample)))
            else:
                additional_sample = []

        except ValueError:
            popular_sample = popular
            unpopular_sample = random.sample(unpopular, k=(10 - len(popular_sample)))
            additional_sample = []
        finally:
            final_projects = popular_sample + unpopular_sample + additional_sample

    random.shuffle(final_projects)
    return final_projects