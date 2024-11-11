from src.yandex_loader.CloudLoaderAbstraction import CloudLoaderAbstraction


class CloudLoader(CloudLoaderAbstraction):
    """Cloud loader implementation
    """

    def get_resource_list(self):
        uri = f"{self.cloud_url}?path={self.cloud_dir}"

        response = self.session.get(uri,
                                    headers=self.headers,
                                    timeout=self.TIMEOUT)

        return response.content, response.status_code
