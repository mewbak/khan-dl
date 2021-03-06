from khan_downloader import *
from interactive_prompt import *
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "-i",
    "--interactive",
    help="Enter Interactive Course Selection Mode",
    dest="interactive_prompt",
    action="store_true",
)
argparser.add_argument(
    "-c", "--course_url", help="Enter Course URL",
)


args = argparser.parse_args()


if args.interactive_prompt:
    selected_course_url = course_selection_prompt()
    khan_down = Khan_DL("", selected_course_url)
    print("Generating Path Slugs..... ")
    khan_down.get_course_html()
    khan_down.generate_unit_slugs()
    khan_down.generate_unit_urls()
    khan_down.generate_course_slugs_video_ids()
    khan_down.download_videos()

if args.course_url:
    print("Looking up " + args.course_url + " .....")
    selected_course_url = args.course_url
    khan_down = Khan_DL("", selected_course_url)

    print("Generating Path Slugs..... ")
    khan_down.get_course_html()
    khan_down.generate_unit_slugs()
    khan_down.generate_unit_urls()
    khan_down.generate_course_slugs_video_ids()
    khan_down.download_videos()
