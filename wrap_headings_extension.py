from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
import xml.etree.ElementTree as etree

class WrapHeadingsProcessor(Treeprocessor):
    def run(self, root):
        """Wrap headings and the first paragraph after them in a <section>."""
        new_root = etree.Element("div")  # Create a new root container for consistent structure
        i = 0

        while i < len(root):
            element = root[i]
            if element.tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
                section = etree.Element("section")  # Create a wrapper section
                section.append(element)  # Add the heading inside
                
                # Check if the next element is a paragraph and add it to the section
                if i + 1 < len(root) and root[i + 1].tag == "p":
                    section.append(root[i + 1])
                    del root[i + 1]  # Remove the paragraph from the main tree
                
                new_root.append(section)  # Add section to the new root
            else:
                new_root.append(element)

            i += 1

        root.clear()
        root.extend(new_root)  # Replace the original root with the modified one

class WrapHeadingsExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(WrapHeadingsProcessor(md), "wrap_headings", 20)


