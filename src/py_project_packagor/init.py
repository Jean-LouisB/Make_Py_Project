class Project:
    def __init__(self):
        project_name = input("Project_name (my_project): ")
        self.project_name = (
            project_name.replace(" ", "_") if project_name != "" else "my_project"
        )
        version = input("Version (1.0.0): ")
        self.version = version if version != "" else "1.0.0"
        description = input("Description (Mon projet Python): ")
        self.description = description if description != "" else "Mon projet Python"
        author_fullname = input("Author fullname (John Lennon): ")
        self.author_fullname = (
            author_fullname.title() if author_fullname != "" else "John Lennon"
        )
        author_email = input("Author email (john.lennon@beatles.uk): ")
        self.author_email = (
            author_email if author_email != "" else "john.lennon@beatles.uk"
        )

        self.author = f"""[
            {{ name = "{self.author_fullname}", email= "{self.author_email}" }},
        ]"""

        self.norm_project_name = self.project_name.lower().replace(" ", "_")
