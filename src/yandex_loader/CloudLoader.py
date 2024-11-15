from .CloudLoaderABC import CloudLoaderABC


class CloudLoader(CloudLoaderABC):
    """Cloud loader implementation
    """

    def get_resource_list(self):
        uri = f"{self.cloud_url}?path={self.cloud_dir}"

        response = self.session.get(uri,
                                    headers=self.headers,
                                    timeout=self.TIMEOUT)

        return response.content, response.status_code
