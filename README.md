# GitHub Pages Deployment

Project URL: https://roadmap.sh/projects/github-pages-deployment

A simple GitHub Actions workflow that automatically deploys a static website to GitHub Pages whenever changes are made to the index.html file.

## Features

- Automated deployment to GitHub Pages
- Triggers only when index.html changes
- Secure deployment using GitHub's OIDC provider
- Automatic URL generation for the deployed site
- Simple and maintainable workflow configuration

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml
├── index.html
└── README.md
```

## Setup Instructions

1. Create a new repository on GitHub:
   - Name it `gh-deployment-workflow` or any name you prefer
   - Make it public
   - Initialize with a README

2. Enable GitHub Pages:
   - Go to repository Settings
   - Navigate to Pages section
   - Under "Source", select "GitHub Actions"

3. Add the workflow file:
   - Create `.github/workflows` directory
   - Create `deploy.yml` inside it
   - Copy the workflow configuration into `deploy.yml`

4. Add the index.html file:
   - Create `index.html` in the root directory
   - Add your static website content

5. Push changes to the main branch:
   ```bash
   git add .
   git commit -m "Initial setup for GitHub Pages deployment"
   git push origin main
   ```

## Workflow Configuration

The workflow (`deploy.yml`) is configured to:
- Trigger on pushes to main branch that modify index.html
- Use GitHub's official actions for deployment
- Set up necessary permissions for GitHub Pages
- Deploy the content to GitHub Pages
- Provide the deployment URL as output

## Testing the Deployment

1. Make a change to index.html
2. Commit and push the change
3. Go to Actions tab in your repository
4. Watch the workflow run
5. Once completed, visit your GitHub Pages URL:
   ```
   https://<username>.github.io/gh-deployment-workflow/
   ```

## Customization

### Adding More Files
To deploy additional files, modify the `path` parameter in the upload step of the workflow:

```yaml
- name: Upload artifact
  uses: actions/upload-pages-artifact@v3
  with:
    path: 'your-build-directory'
```

### Using Static Site Generators
For static site generators (Hugo, Jekyll, Astro), add build steps before deployment:

```yaml
- name: Setup Node.js (for Astro)
  uses: actions/setup-node@v3
  with:
    node-version: '18'

- name: Install dependencies
  run: npm install

- name: Build site
  run: npm run build
```

## Troubleshooting

Common issues and solutions:

1. **Workflow Not Triggering**
   - Ensure changes are pushed to the main branch
   - Verify the file path in the workflow trigger matches your structure

2. **Deployment Failed**
   - Check if GitHub Pages is enabled in repository settings
   - Verify the required permissions are set in the workflow

3. **Page Not Accessible**
   - Wait a few minutes for DNS propagation
   - Verify the repository is public
   - Check the deployment URL in the Actions tab

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name]
[Your Contact Information]

## Acknowledgments

- GitHub Actions and Pages documentation
- GitHub Actions official examples
- Static site deployment best practices