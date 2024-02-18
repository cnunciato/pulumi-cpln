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

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 spec: pulumi.Input['DomainSpecArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Domain resource.
        """
        DomainArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            spec=spec,
            description=description,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             spec: pulumi.Input['DomainSpecArgs'],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("spec", spec)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input['DomainSpecArgs']:
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input['DomainSpecArgs']):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *,
                 cpln_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input['DomainSpecArgs']] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input['DomainStatusArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Domain resources.
        """
        _DomainState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cpln_id=cpln_id,
            description=description,
            name=name,
            self_link=self_link,
            spec=spec,
            statuses=statuses,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cpln_id: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             self_link: Optional[pulumi.Input[str]] = None,
             spec: Optional[pulumi.Input['DomainSpecArgs']] = None,
             statuses: Optional[pulumi.Input[Sequence[pulumi.Input['DomainStatusArgs']]]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'cplnId' in kwargs:
            cpln_id = kwargs['cplnId']
        if 'selfLink' in kwargs:
            self_link = kwargs['selfLink']

        if cpln_id is not None:
            _setter("cpln_id", cpln_id)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if self_link is not None:
            _setter("self_link", self_link)
        if spec is not None:
            _setter("spec", spec)
        if statuses is not None:
            _setter("statuses", statuses)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="cplnId")
    def cpln_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cpln_id")

    @cpln_id.setter
    def cpln_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cpln_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input['DomainSpecArgs']]:
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input['DomainSpecArgs']]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainStatusArgs']]]]:
        return pulumi.get(self, "statuses")

    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainStatusArgs']]]]):
        pulumi.set(self, "statuses", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['DomainSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DomainArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['DomainSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if spec is not None and not isinstance(spec, DomainSpecArgs):
                spec = spec or {}
                def _setter(key, value):
                    spec[key] = value
                DomainSpecArgs._configure(_setter, **spec)
            if spec is None and not opts.urn:
                raise TypeError("Missing required property 'spec'")
            __props__.__dict__["spec"] = spec
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cpln_id"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["statuses"] = None
        super(Domain, __self__).__init__(
            'cpln:index/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cpln_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            spec: Optional[pulumi.Input[pulumi.InputType['DomainSpecArgs']]] = None,
            statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainStatusArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainState.__new__(_DomainState)

        __props__.__dict__["cpln_id"] = cpln_id
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["spec"] = spec
        __props__.__dict__["statuses"] = statuses
        __props__.__dict__["tags"] = tags
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cplnId")
    def cpln_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cpln_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.DomainSpec']:
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence['outputs.DomainStatus']]:
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")
