# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple


from google.api_core import gapic_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.auth.transport.requests import AuthorizedSession


from google.cloud.compute_v1.types import compute


from .base import TargetHttpProxiesTransport, DEFAULT_CLIENT_INFO


class TargetHttpProxiesRestTransport(TargetHttpProxiesTransport):
    """REST backend transport for TargetHttpProxies.

    The TargetHttpProxies API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        super().__init__(
            host=host, credentials=credentials, client_info=client_info,
        )
        self._session = AuthorizedSession(self._credentials)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)

    def aggregated_list(
        self,
        request: compute.AggregatedListTargetHttpProxiesRequest,
        *,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.TargetHttpProxyAggregatedList:
        r"""Call the aggregated list method over HTTP.

        Args:
            request (~.compute.AggregatedListTargetHttpProxiesRequest):
                The request object.
                A request message for
                TargetHttpProxies.AggregatedList. See
                the method description for details.

            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.TargetHttpProxyAggregatedList:

        """

        # TODO(yon-mg): need to handle grpc transcoding and parse url correctly
        #               current impl assumes basic case of grpc transcoding
        url = "https://{host}/compute/v1/projects/{project}/aggregated/targetHttpProxies".format(
            host=self._host, project=request.project,
        )

        # TODO(yon-mg): handle nested fields corerctly rather than using only top level fields
        #               not required for GCE
        query_params = {
            "filter": request.filter,
            "pageToken": request.page_token,
            "returnPartialSuccess": request.return_partial_success,
            "maxResults": request.max_results,
            "includeAllScopes": request.include_all_scopes,
            "orderBy": request.order_by,
        }
        # TODO(yon-mg): further discussion needed whether 'python truthiness' is appropriate here
        #               discards default values
        # TODO(yon-mg): add test for proper url encoded strings
        query_params = [
            "{k}={v}".format(k=k, v=v) for k, v in query_params.items() if v
        ]
        url += "?{}".format("&".join(query_params)).replace(" ", "+")

        # Send the request
        response = self._session.get(url)

        # Raise requests.exceptions.HTTPError if the status code is >= 400
        response.raise_for_status()

        # Return the response
        return compute.TargetHttpProxyAggregatedList.from_json(response.content)

    def delete(
        self,
        request: compute.DeleteTargetHttpProxyRequest,
        *,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Call the delete method over HTTP.

        Args:
            request (~.compute.DeleteTargetHttpProxyRequest):
                The request object.
                A request message for
                TargetHttpProxies.Delete. See the method
                description for details.

            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.Operation:
                Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                -  `Global </compute/docs/reference/rest/{$api_version}/globalOperations>`__
                   \*
                   `Regional </compute/docs/reference/rest/{$api_version}/regionOperations>`__
                   \*
                   `Zonal </compute/docs/reference/rest/{$api_version}/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses.

                Operations can be global, regional or zonal.

                -  For global operations, use the ``globalOperations``
                   resource.
                -  For regional operations, use the ``regionOperations``
                   resource.
                -  For zonal operations, use the ``zonalOperations``
                   resource.

                For more information, read Global, Regional, and Zonal
                Resources. (== resource_for
                {$api_version}.globalOperations ==) (== resource_for
                {$api_version}.regionOperations ==) (== resource_for
                {$api_version}.zoneOperations ==)

        """

        # TODO(yon-mg): need to handle grpc transcoding and parse url correctly
        #               current impl assumes basic case of grpc transcoding
        url = "https://{host}/compute/v1/projects/{project}/global/targetHttpProxies/{target_http_proxy}".format(
            host=self._host,
            project=request.project,
            target_http_proxy=request.target_http_proxy,
        )

        # TODO(yon-mg): handle nested fields corerctly rather than using only top level fields
        #               not required for GCE
        query_params = {
            "requestId": request.request_id,
        }
        # TODO(yon-mg): further discussion needed whether 'python truthiness' is appropriate here
        #               discards default values
        # TODO(yon-mg): add test for proper url encoded strings
        query_params = [
            "{k}={v}".format(k=k, v=v) for k, v in query_params.items() if v
        ]
        url += "?{}".format("&".join(query_params)).replace(" ", "+")

        # Send the request
        response = self._session.delete(url)

        # Raise requests.exceptions.HTTPError if the status code is >= 400
        response.raise_for_status()

        # Return the response
        return compute.Operation.from_json(response.content)

    def get(
        self,
        request: compute.GetTargetHttpProxyRequest,
        *,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.TargetHttpProxy:
        r"""Call the get method over HTTP.

        Args:
            request (~.compute.GetTargetHttpProxyRequest):
                The request object.
                A request message for
                TargetHttpProxies.Get. See the method
                description for details.

            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.TargetHttpProxy:
                Represents a Target HTTP Proxy resource.

                Google Compute Engine has two Target HTTP Proxy
                resources:

                -  `Global </compute/docs/reference/rest/{$api_version}/targetHttpProxies>`__
                   \*
                   `Regional </compute/docs/reference/rest/{$api_version}/regionTargetHttpProxies>`__

                A target HTTP proxy is a component of GCP HTTP load
                balancers.

                -  targetHttpProxies are used by external HTTP load
                   balancers and Traffic Director. \*
                   regionTargetHttpProxies are used by internal HTTP
                   load balancers.

                Forwarding rules reference a target HTTP proxy, and the
                target proxy then references a URL map. For more
                information, read Using Target Proxies and Forwarding
                rule concepts. (== resource_for
                {$api_version}.targetHttpProxies ==) (== resource_for
                {$api_version}.regionTargetHttpProxies ==)

        """

        # TODO(yon-mg): need to handle grpc transcoding and parse url correctly
        #               current impl assumes basic case of grpc transcoding
        url = "https://{host}/compute/v1/projects/{project}/global/targetHttpProxies/{target_http_proxy}".format(
            host=self._host,
            project=request.project,
            target_http_proxy=request.target_http_proxy,
        )

        # TODO(yon-mg): handle nested fields corerctly rather than using only top level fields
        #               not required for GCE
        query_params = {}
        # TODO(yon-mg): further discussion needed whether 'python truthiness' is appropriate here
        #               discards default values
        # TODO(yon-mg): add test for proper url encoded strings
        query_params = [
            "{k}={v}".format(k=k, v=v) for k, v in query_params.items() if v
        ]
        url += "?{}".format("&".join(query_params)).replace(" ", "+")

        # Send the request
        response = self._session.get(url)

        # Raise requests.exceptions.HTTPError if the status code is >= 400
        response.raise_for_status()

        # Return the response
        return compute.TargetHttpProxy.from_json(response.content)

    def insert(
        self,
        request: compute.InsertTargetHttpProxyRequest,
        *,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Call the insert method over HTTP.

        Args:
            request (~.compute.InsertTargetHttpProxyRequest):
                The request object.
                A request message for
                TargetHttpProxies.Insert. See the method
                description for details.

            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.Operation:
                Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                -  `Global </compute/docs/reference/rest/{$api_version}/globalOperations>`__
                   \*
                   `Regional </compute/docs/reference/rest/{$api_version}/regionOperations>`__
                   \*
                   `Zonal </compute/docs/reference/rest/{$api_version}/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses.

                Operations can be global, regional or zonal.

                -  For global operations, use the ``globalOperations``
                   resource.
                -  For regional operations, use the ``regionOperations``
                   resource.
                -  For zonal operations, use the ``zonalOperations``
                   resource.

                For more information, read Global, Regional, and Zonal
                Resources. (== resource_for
                {$api_version}.globalOperations ==) (== resource_for
                {$api_version}.regionOperations ==) (== resource_for
                {$api_version}.zoneOperations ==)

        """

        # Jsonify the request body
        body = compute.TargetHttpProxy.to_json(
            request.target_http_proxy_resource, including_default_value_fields=False
        )

        # TODO(yon-mg): need to handle grpc transcoding and parse url correctly
        #               current impl assumes basic case of grpc transcoding
        url = "https://{host}/compute/v1/projects/{project}/global/targetHttpProxies".format(
            host=self._host, project=request.project,
        )

        # TODO(yon-mg): handle nested fields corerctly rather than using only top level fields
        #               not required for GCE
        query_params = {
            "requestId": request.request_id,
        }
        # TODO(yon-mg): further discussion needed whether 'python truthiness' is appropriate here
        #               discards default values
        # TODO(yon-mg): add test for proper url encoded strings
        query_params = [
            "{k}={v}".format(k=k, v=v) for k, v in query_params.items() if v
        ]
        url += "?{}".format("&".join(query_params)).replace(" ", "+")

        # Send the request
        response = self._session.post(url, json=body,)

        # Raise requests.exceptions.HTTPError if the status code is >= 400
        response.raise_for_status()

        # Return the response
        return compute.Operation.from_json(response.content)

    def list(
        self,
        request: compute.ListTargetHttpProxiesRequest,
        *,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.TargetHttpProxyList:
        r"""Call the list method over HTTP.

        Args:
            request (~.compute.ListTargetHttpProxiesRequest):
                The request object.
                A request message for
                TargetHttpProxies.List. See the method
                description for details.

            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.TargetHttpProxyList:
                A list of TargetHttpProxy resources.
        """

        # TODO(yon-mg): need to handle grpc transcoding and parse url correctly
        #               current impl assumes basic case of grpc transcoding
        url = "https://{host}/compute/v1/projects/{project}/global/targetHttpProxies".format(
            host=self._host, project=request.project,
        )

        # TODO(yon-mg): handle nested fields corerctly rather than using only top level fields
        #               not required for GCE
        query_params = {
            "filter": request.filter,
            "pageToken": request.page_token,
            "returnPartialSuccess": request.return_partial_success,
            "maxResults": request.max_results,
            "orderBy": request.order_by,
        }
        # TODO(yon-mg): further discussion needed whether 'python truthiness' is appropriate here
        #               discards default values
        # TODO(yon-mg): add test for proper url encoded strings
        query_params = [
            "{k}={v}".format(k=k, v=v) for k, v in query_params.items() if v
        ]
        url += "?{}".format("&".join(query_params)).replace(" ", "+")

        # Send the request
        response = self._session.get(url)

        # Raise requests.exceptions.HTTPError if the status code is >= 400
        response.raise_for_status()

        # Return the response
        return compute.TargetHttpProxyList.from_json(response.content)

    def patch(
        self,
        request: compute.PatchTargetHttpProxyRequest,
        *,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Call the patch method over HTTP.

        Args:
            request (~.compute.PatchTargetHttpProxyRequest):
                The request object.
                A request message for
                TargetHttpProxies.Patch. See the method
                description for details.

            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.Operation:
                Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                -  `Global </compute/docs/reference/rest/{$api_version}/globalOperations>`__
                   \*
                   `Regional </compute/docs/reference/rest/{$api_version}/regionOperations>`__
                   \*
                   `Zonal </compute/docs/reference/rest/{$api_version}/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses.

                Operations can be global, regional or zonal.

                -  For global operations, use the ``globalOperations``
                   resource.
                -  For regional operations, use the ``regionOperations``
                   resource.
                -  For zonal operations, use the ``zonalOperations``
                   resource.

                For more information, read Global, Regional, and Zonal
                Resources. (== resource_for
                {$api_version}.globalOperations ==) (== resource_for
                {$api_version}.regionOperations ==) (== resource_for
                {$api_version}.zoneOperations ==)

        """

        # Jsonify the request body
        body = compute.TargetHttpProxy.to_json(
            request.target_http_proxy_resource, including_default_value_fields=False
        )

        # TODO(yon-mg): need to handle grpc transcoding and parse url correctly
        #               current impl assumes basic case of grpc transcoding
        url = "https://{host}/compute/v1/projects/{project}/global/targetHttpProxies/{target_http_proxy}".format(
            host=self._host,
            project=request.project,
            target_http_proxy=request.target_http_proxy,
        )

        # TODO(yon-mg): handle nested fields corerctly rather than using only top level fields
        #               not required for GCE
        query_params = {
            "requestId": request.request_id,
        }
        # TODO(yon-mg): further discussion needed whether 'python truthiness' is appropriate here
        #               discards default values
        # TODO(yon-mg): add test for proper url encoded strings
        query_params = [
            "{k}={v}".format(k=k, v=v) for k, v in query_params.items() if v
        ]
        url += "?{}".format("&".join(query_params)).replace(" ", "+")

        # Send the request
        response = self._session.patch(url, json=body,)

        # Raise requests.exceptions.HTTPError if the status code is >= 400
        response.raise_for_status()

        # Return the response
        return compute.Operation.from_json(response.content)

    def set_url_map(
        self,
        request: compute.SetUrlMapTargetHttpProxyRequest,
        *,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Call the set url map method over HTTP.

        Args:
            request (~.compute.SetUrlMapTargetHttpProxyRequest):
                The request object.
                A request message for
                TargetHttpProxies.SetUrlMap. See the
                method description for details.

            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.Operation:
                Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                -  `Global </compute/docs/reference/rest/{$api_version}/globalOperations>`__
                   \*
                   `Regional </compute/docs/reference/rest/{$api_version}/regionOperations>`__
                   \*
                   `Zonal </compute/docs/reference/rest/{$api_version}/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses.

                Operations can be global, regional or zonal.

                -  For global operations, use the ``globalOperations``
                   resource.
                -  For regional operations, use the ``regionOperations``
                   resource.
                -  For zonal operations, use the ``zonalOperations``
                   resource.

                For more information, read Global, Regional, and Zonal
                Resources. (== resource_for
                {$api_version}.globalOperations ==) (== resource_for
                {$api_version}.regionOperations ==) (== resource_for
                {$api_version}.zoneOperations ==)

        """

        # Jsonify the request body
        body = compute.UrlMapReference.to_json(
            request.url_map_reference_resource, including_default_value_fields=False
        )

        # TODO(yon-mg): need to handle grpc transcoding and parse url correctly
        #               current impl assumes basic case of grpc transcoding
        url = "https://{host}/compute/v1/projects/{project}/targetHttpProxies/{target_http_proxy}/setUrlMap".format(
            host=self._host,
            project=request.project,
            target_http_proxy=request.target_http_proxy,
        )

        # TODO(yon-mg): handle nested fields corerctly rather than using only top level fields
        #               not required for GCE
        query_params = {
            "requestId": request.request_id,
        }
        # TODO(yon-mg): further discussion needed whether 'python truthiness' is appropriate here
        #               discards default values
        # TODO(yon-mg): add test for proper url encoded strings
        query_params = [
            "{k}={v}".format(k=k, v=v) for k, v in query_params.items() if v
        ]
        url += "?{}".format("&".join(query_params)).replace(" ", "+")

        # Send the request
        response = self._session.post(url, json=body,)

        # Raise requests.exceptions.HTTPError if the status code is >= 400
        response.raise_for_status()

        # Return the response
        return compute.Operation.from_json(response.content)


__all__ = ("TargetHttpProxiesRestTransport",)
