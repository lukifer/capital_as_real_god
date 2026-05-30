from markdown.inlinepatterns import IMAGE_LINK_RE, ImageInlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

class FigureCaptionProcessor(ImageInlineProcessor):
    def handleMatch(self, m, data):
        el, start, end = super().handleMatch(m, data)  # Unpack the tuple correctly

        if el is not None and "title" in el.attrib:
            caption_text = el.attrib.pop("title", None)
            if caption_text:
                # Create <figure> wrapper
                figure = etree.Element("figure")
                figure.append(el)  # Add <img> inside <figure>

                # Create <figcaption> with the extracted title
                figcaption = etree.Element("figcaption")
                figcaption.text = caption_text
                figure.append(figcaption)  # Add <figcaption> inside <figure>

				# Ya gotta keep em separated
                br = etree.Element("br")
                figure.append(br)  # Add <br> inside <figure>

                return figure, start, end  # Return the correct tuple format

        return el, start, end  # Ensure correct return format even if no caption is present

class FigureCaptionExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(FigureCaptionProcessor(IMAGE_LINK_RE, md), "figure_caption", 175)
