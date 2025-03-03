# Blog CMS

A simple Content Management System for your Jekyll blog.

## Features

- Create, edit, and delete blog posts
- Markdown editor with preview
- Image upload support
- Categories and tags management
- Automatic frontmatter handling

## Setup

1. Clone this repository next to your Jekyll blog:
```bash
git clone https://github.com/yourusername/blog-cms.git
cd blog-cms
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and configure your settings:
```bash
cp .env.example .env
```

4. Edit `.env` with your credentials and paths:
```
SECRET_KEY=your-secret-key
ADMIN_USERNAME=your-username
ADMIN_PASSWORD=your-password
BLOG_PATH=path/to/your/jekyll/blog
GITHUB_TOKEN=your-github-token
GITHUB_USERNAME=your-github-username
```

5. Run the application:
```bash
python run.py
```

6. Visit `http://localhost:5000` and log in with your credentials.

## Usage

1. **Creating a Post**
   - Click "New Post" in the sidebar
   - Fill in the title, categories, and tags
   - Write your content in Markdown
   - Click "Save" to create the post

2. **Editing a Post**
   - Click "Posts" in the sidebar
   - Find the post you want to edit
   - Click "Edit"
   - Make your changes
   - Click "Save"

3. **Uploading Images**
   - While editing a post, click the image button in the editor
   - Select your image file
   - The image will be uploaded and inserted into your post

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 