from pybry import LbrydApi

class LBRYUploader:
    def __init__(self):
        self.lbry = LbrydApi()

    def upload(self, video_info):
        """
        Upload the video to LBRY.

        Args:
            video_info (dict): The video information dictionary.

        Returns:
            str: The LBRY URL of the uploaded video, or None if the upload failed.
        """
        try:
            lbry_results = self.lbry.publish(
                name=video_info['id'], preview=False, blocking=True, bid='0.001',
                file_path=video_info['download_path'],
                channel_id="68dad212fddb3d6cb294278e11a303a6a98f2905",
                thumbnail_url=video_info['thumbnail'],
                title=video_info['title'], description=video_info['description']
            )
            return lbry_results[0]['outputs'][0]['permanent_url']
        except Exception as e:
            print(f"Error uploading video to LBRY: {e}")
            if hasattr(e, 'response'):
                print(f"LBRY API Response: {e.response}")
            return None
   
