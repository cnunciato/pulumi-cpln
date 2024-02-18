# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetOrgResult',
    'AwaitableGetOrgResult',
    'get_org',
    'get_org_output',
]

@pulumi.output_type
class GetOrgResult:
    """
    A collection of values returned by getOrg.
    """
    def __init__(__self__, cpln_id=None, id=None, name=None):
        if cpln_id and not isinstance(cpln_id, str):
            raise TypeError("Expected argument 'cpln_id' to be a str")
        pulumi.set(__self__, "cpln_id", cpln_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="cplnId")
    def cpln_id(self) -> str:
        return pulumi.get(self, "cpln_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetOrgResult(GetOrgResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrgResult(
            cpln_id=self.cpln_id,
            id=self.id,
            name=self.name)


def get_org(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrgResult:
    """
    Output the ID and name of the current [org](https://docs.controlplane.com/reference/org).

    ## Outputs

    The following attributes are exported:

    - **cpln_id** (String) The ID, in GUID format, of the Org.
    - **name** (String) The name of Org.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cpln as cpln

    org = cpln.get_org()
    pulumi.export("orgId", org.id)
    pulumi.export("orgName", org.name)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cpln:index/getOrg:getOrg', __args__, opts=opts, typ=GetOrgResult).value

    return AwaitableGetOrgResult(
        cpln_id=pulumi.get(__ret__, 'cpln_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_org)
def get_org_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrgResult]:
    """
    Output the ID and name of the current [org](https://docs.controlplane.com/reference/org).

    ## Outputs

    The following attributes are exported:

    - **cpln_id** (String) The ID, in GUID format, of the Org.
    - **name** (String) The name of Org.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cpln as cpln

    org = cpln.get_org()
    pulumi.export("orgId", org.id)
    pulumi.export("orgName", org.name)
    ```
    """
    ...