from apps.portfolio.models import Project


class DataController():

    @staticmethod
    def get_all_projects():

        qs_projects = Project.projectobjects.all()
        print(qs_projects)
        for project in qs_projects:
            print(project.slug)

        return qs_projects