from blog import Blog

blogs = dict()

MENU_PROMPT = "Options: \n'c' to create a blog\n'l' to list blogs\n'r' to read one\n'p' to create a post\n'q' to quit\n"

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()

        selection = input(MENU_PROMPT)

def print_blogs():
    # print the available blogs
    for blog in blogs:
        print(f'- {blog}')
    

def ask_create_blog():
    # aqui será aplicado o side_effect[0]
    title = input('Insert the Blog Title:\n')
    
    # aqui será aplicado o side_effect[1]
    author = input("Insert the Blog Author's name:\n")
    
    blogs[title] = Blog(title, author)


def ask_read_blog():
    blog_name = input("Insert the Blog's name:\n")
    
    if blog_name in blogs:
        print(f"Reading the {blog_name}'s posts:\n")
        for post in blogs[blog_name].posts:
            print(f'Title: {post.title}\nContent: {post.content}\n\n')

    else:
        answer = input('This blog does not exist, would you like to create it? <y/n>\n')

        if answer == 'y':
            author_name = input("Enter the author's name:\n")

            blogs[blog_name] = Blog(blog_name, author_name)


def ask_create_post():
    blog_name = input("Insert the blog's name that you want to post to:\n")

    if blog_name in blogs:
        post_title = input("Insert your post's title:\n")
        post_content = input("Insert your post's content:\n")

        blogs[blog_name].create_post(post_title, post_content)

    else: 
        answer = input('This blog does not exist, would you like to create it? <y/n>\n')

        if answer == 'y':
            author_name = input("Enter the author's name:\n")

            blogs[blog_name] = Blog(blog_name, author_name)
