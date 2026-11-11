class Default:
    project_name = "my_project"
    version = "1.0.0"
    description = "Mon projet Python"
    author = "John Lennon"
    email = "john.lennon@beatles.uk"


class Project:
    def __init__(self):
        project_name = input(f"\nProject_name ({Default.project_name}): ")
        version = input(f"Version ({Default.version}): ")
        description = input(f"Description ({Default.description}): ")
        author_fullname = input(f"Author fullname ({Default.author}): ")
        author_email = input(f"Author email ({Default.email}): ")

        self.project_name = (
            project_name.replace(" ", "_")
            if project_name != ""
            else Default.project_name
        )
        self.version = version if version != "" else Default.version
        self.description = description if description != "" else Default.description
        self.author_fullname = (
            author_fullname.title() if author_fullname != "" else Default.author
        )
        self.author_email = author_email if author_email != "" else Default.email

        print("\n✅ Initialisation terminée.\n")

    @property
    def norm_project_name(self):
        return self.project_name.lower().replace(" ", "_")

    @property
    def author_to_dict(self):
        return f"""[
            {{ name = "{self.author_fullname}", email= "{self.author_email}" }},
        ]"""
