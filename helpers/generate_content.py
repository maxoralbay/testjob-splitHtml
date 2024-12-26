# Generating a large HTML content with random placeholder text.
import lorem

# Generate placeholder text
section_content = lorem.text() * 100  # Roughly generate a long text content

# Create the HTML structure
html_content = """
<p>
  <b>
    <a href="https://www.google.com/">Google search</a>
    <ul>
      <li>{}</li>
      <li>{}</li>
      <li>{}</li>
    </ul>
  </b>
</p>
""".format(section_content[:4096], section_content[4096:8192], section_content[8192:12288])

# Save the file
file_path = 'large_html_content.html'
with open(file_path, 'w') as file:
    file.write(html_content)
