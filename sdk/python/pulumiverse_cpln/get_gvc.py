# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetGvcResult',
    'AwaitableGetGvcResult',
    'get_gvc',
    'get_gvc_output',
]

@pulumi.output_type
class GetGvcResult:
    """
    A collection of values returned by getGvc.
    """
    def __init__(__self__, alias=None, controlplane_tracing=None, cpln_id=None, description=None, domain=None, env=None, id=None, lightstep_tracing=None, load_balancer=None, locations=None, name=None, otel_tracing=None, pull_secrets=None, self_link=None, sidecar=None, tags=None):
        if alias and not isinstance(alias, str):
            raise TypeError("Expected argument 'alias' to be a str")
        pulumi.set(__self__, "alias", alias)
        if controlplane_tracing and not isinstance(controlplane_tracing, dict):
            raise TypeError("Expected argument 'controlplane_tracing' to be a dict")
        pulumi.set(__self__, "controlplane_tracing", controlplane_tracing)
        if cpln_id and not isinstance(cpln_id, str):
            raise TypeError("Expected argument 'cpln_id' to be a str")
        pulumi.set(__self__, "cpln_id", cpln_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if env and not isinstance(env, dict):
            raise TypeError("Expected argument 'env' to be a dict")
        pulumi.set(__self__, "env", env)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lightstep_tracing and not isinstance(lightstep_tracing, dict):
            raise TypeError("Expected argument 'lightstep_tracing' to be a dict")
        pulumi.set(__self__, "lightstep_tracing", lightstep_tracing)
        if load_balancer and not isinstance(load_balancer, dict):
            raise TypeError("Expected argument 'load_balancer' to be a dict")
        pulumi.set(__self__, "load_balancer", load_balancer)
        if locations and not isinstance(locations, list):
            raise TypeError("Expected argument 'locations' to be a list")
        pulumi.set(__self__, "locations", locations)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if otel_tracing and not isinstance(otel_tracing, dict):
            raise TypeError("Expected argument 'otel_tracing' to be a dict")
        pulumi.set(__self__, "otel_tracing", otel_tracing)
        if pull_secrets and not isinstance(pull_secrets, list):
            raise TypeError("Expected argument 'pull_secrets' to be a list")
        pulumi.set(__self__, "pull_secrets", pull_secrets)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if sidecar and not isinstance(sidecar, dict):
            raise TypeError("Expected argument 'sidecar' to be a dict")
        pulumi.set(__self__, "sidecar", sidecar)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def alias(self) -> str:
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="controlplaneTracing")
    def controlplane_tracing(self) -> Optional['outputs.GetGvcControlplaneTracingResult']:
        return pulumi.get(self, "controlplane_tracing")

    @property
    @pulumi.getter(name="cplnId")
    def cpln_id(self) -> str:
        return pulumi.get(self, "cpln_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        warnings.warn("""Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.""", DeprecationWarning)
        pulumi.log.warn("""domain is deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.""")

        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def env(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "env")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lightstepTracing")
    def lightstep_tracing(self) -> Optional['outputs.GetGvcLightstepTracingResult']:
        return pulumi.get(self, "lightstep_tracing")

    @property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional['outputs.GetGvcLoadBalancerResult']:
        return pulumi.get(self, "load_balancer")

    @property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="otelTracing")
    def otel_tracing(self) -> Optional['outputs.GetGvcOtelTracingResult']:
        return pulumi.get(self, "otel_tracing")

    @property
    @pulumi.getter(name="pullSecrets")
    def pull_secrets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "pull_secrets")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def sidecar(self) -> Optional['outputs.GetGvcSidecarResult']:
        return pulumi.get(self, "sidecar")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")


class AwaitableGetGvcResult(GetGvcResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGvcResult(
            alias=self.alias,
            controlplane_tracing=self.controlplane_tracing,
            cpln_id=self.cpln_id,
            description=self.description,
            domain=self.domain,
            env=self.env,
            id=self.id,
            lightstep_tracing=self.lightstep_tracing,
            load_balancer=self.load_balancer,
            locations=self.locations,
            name=self.name,
            otel_tracing=self.otel_tracing,
            pull_secrets=self.pull_secrets,
            self_link=self.self_link,
            sidecar=self.sidecar,
            tags=self.tags)


def get_gvc(controlplane_tracing: Optional[pulumi.InputType['GetGvcControlplaneTracingArgs']] = None,
            description: Optional[str] = None,
            domain: Optional[str] = None,
            env: Optional[Mapping[str, str]] = None,
            lightstep_tracing: Optional[pulumi.InputType['GetGvcLightstepTracingArgs']] = None,
            load_balancer: Optional[pulumi.InputType['GetGvcLoadBalancerArgs']] = None,
            locations: Optional[Sequence[str]] = None,
            name: Optional[str] = None,
            otel_tracing: Optional[pulumi.InputType['GetGvcOtelTracingArgs']] = None,
            pull_secrets: Optional[Sequence[str]] = None,
            sidecar: Optional[pulumi.InputType['GetGvcSidecarArgs']] = None,
            tags: Optional[Mapping[str, str]] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGvcResult:
    """
    Use this data source to access information about an existing [Global Virtual Cloud (GVC)](https://docs.controlplane.com/reference/gvc) within Control Plane.

    ## Required

    - **name** (String) Name of the GVC.

    ## Outputs

    The following attributes are exported:

    - **cpln_id** (String) The ID, in GUID format, of the GVC.
    - **name** (String) Name of the GVC.
    - **locations** (List of String) A list of [locations](https://docs.controlplane.com/reference/location#current) making up the Global Virtual Cloud.
    - **description** (String) Description of the GVC.
    - **domain** (String) Custom domain name used by associated workloads.
    - **pull_secrets** (List of String) A list of [pull secret](https://docs.controlplane.com/reference/gvc#pull-secrets) names used to authenticate to any private image repository referenced by Workloads within the GVC.
    - **tags** (Map of String) Key-value map of resource tags.
    - **lightstep_tracing** (Block List, Max: 1) (see below).
    - **self_link** (String) Full link to this resource. Can be referenced by other resources.

    <a id="nestedblock--lightstep_tracing"></a>
    ### `lightstep_tracing`

    - **sampling** (Int) Sampling percentage.
    - **endpoint** (String) Tracing Endpoint Workload. Either the canonical endpoint or the internal endpoint.
    - **credentials** (String) Full link to referenced Opaque Secret.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cpln as cpln

    gvc = cpln.get_gvc()
    pulumi.export("gvcId", gvc.id)
    pulumi.export("gvcLocations", gvc.locations)
    ```
    """
    __args__ = dict()
    __args__['controlplaneTracing'] = controlplane_tracing
    __args__['description'] = description
    __args__['domain'] = domain
    __args__['env'] = env
    __args__['lightstepTracing'] = lightstep_tracing
    __args__['loadBalancer'] = load_balancer
    __args__['locations'] = locations
    __args__['name'] = name
    __args__['otelTracing'] = otel_tracing
    __args__['pullSecrets'] = pull_secrets
    __args__['sidecar'] = sidecar
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cpln:index/getGvc:getGvc', __args__, opts=opts, typ=GetGvcResult).value

    return AwaitableGetGvcResult(
        alias=pulumi.get(__ret__, 'alias'),
        controlplane_tracing=pulumi.get(__ret__, 'controlplane_tracing'),
        cpln_id=pulumi.get(__ret__, 'cpln_id'),
        description=pulumi.get(__ret__, 'description'),
        domain=pulumi.get(__ret__, 'domain'),
        env=pulumi.get(__ret__, 'env'),
        id=pulumi.get(__ret__, 'id'),
        lightstep_tracing=pulumi.get(__ret__, 'lightstep_tracing'),
        load_balancer=pulumi.get(__ret__, 'load_balancer'),
        locations=pulumi.get(__ret__, 'locations'),
        name=pulumi.get(__ret__, 'name'),
        otel_tracing=pulumi.get(__ret__, 'otel_tracing'),
        pull_secrets=pulumi.get(__ret__, 'pull_secrets'),
        self_link=pulumi.get(__ret__, 'self_link'),
        sidecar=pulumi.get(__ret__, 'sidecar'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_gvc)
def get_gvc_output(controlplane_tracing: Optional[pulumi.Input[Optional[pulumi.InputType['GetGvcControlplaneTracingArgs']]]] = None,
                   description: Optional[pulumi.Input[Optional[str]]] = None,
                   domain: Optional[pulumi.Input[Optional[str]]] = None,
                   env: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                   lightstep_tracing: Optional[pulumi.Input[Optional[pulumi.InputType['GetGvcLightstepTracingArgs']]]] = None,
                   load_balancer: Optional[pulumi.Input[Optional[pulumi.InputType['GetGvcLoadBalancerArgs']]]] = None,
                   locations: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                   name: Optional[pulumi.Input[str]] = None,
                   otel_tracing: Optional[pulumi.Input[Optional[pulumi.InputType['GetGvcOtelTracingArgs']]]] = None,
                   pull_secrets: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                   sidecar: Optional[pulumi.Input[Optional[pulumi.InputType['GetGvcSidecarArgs']]]] = None,
                   tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGvcResult]:
    """
    Use this data source to access information about an existing [Global Virtual Cloud (GVC)](https://docs.controlplane.com/reference/gvc) within Control Plane.

    ## Required

    - **name** (String) Name of the GVC.

    ## Outputs

    The following attributes are exported:

    - **cpln_id** (String) The ID, in GUID format, of the GVC.
    - **name** (String) Name of the GVC.
    - **locations** (List of String) A list of [locations](https://docs.controlplane.com/reference/location#current) making up the Global Virtual Cloud.
    - **description** (String) Description of the GVC.
    - **domain** (String) Custom domain name used by associated workloads.
    - **pull_secrets** (List of String) A list of [pull secret](https://docs.controlplane.com/reference/gvc#pull-secrets) names used to authenticate to any private image repository referenced by Workloads within the GVC.
    - **tags** (Map of String) Key-value map of resource tags.
    - **lightstep_tracing** (Block List, Max: 1) (see below).
    - **self_link** (String) Full link to this resource. Can be referenced by other resources.

    <a id="nestedblock--lightstep_tracing"></a>
    ### `lightstep_tracing`

    - **sampling** (Int) Sampling percentage.
    - **endpoint** (String) Tracing Endpoint Workload. Either the canonical endpoint or the internal endpoint.
    - **credentials** (String) Full link to referenced Opaque Secret.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cpln as cpln

    gvc = cpln.get_gvc()
    pulumi.export("gvcId", gvc.id)
    pulumi.export("gvcLocations", gvc.locations)
    ```
    """
    ...
