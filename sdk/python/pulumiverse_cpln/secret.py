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

__all__ = ['SecretArgs', 'Secret']

@pulumi.input_type
class SecretArgs:
    def __init__(__self__, *,
                 aws: Optional[pulumi.Input['SecretAwsArgs']] = None,
                 azure_connector: Optional[pulumi.Input['SecretAzureConnectorArgs']] = None,
                 azure_sdk: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dictionary: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 docker: Optional[pulumi.Input[str]] = None,
                 ecr: Optional[pulumi.Input['SecretEcrArgs']] = None,
                 gcp: Optional[pulumi.Input[str]] = None,
                 keypair: Optional[pulumi.Input['SecretKeypairArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nats_account: Optional[pulumi.Input['SecretNatsAccountArgs']] = None,
                 opaque: Optional[pulumi.Input['SecretOpaqueArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tls: Optional[pulumi.Input['SecretTlsArgs']] = None,
                 userpass: Optional[pulumi.Input['SecretUserpassArgs']] = None):
        """
        The set of arguments for constructing a Secret resource.
        """
        SecretArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            aws=aws,
            azure_connector=azure_connector,
            azure_sdk=azure_sdk,
            description=description,
            dictionary=dictionary,
            docker=docker,
            ecr=ecr,
            gcp=gcp,
            keypair=keypair,
            name=name,
            nats_account=nats_account,
            opaque=opaque,
            tags=tags,
            tls=tls,
            userpass=userpass,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             aws: Optional[pulumi.Input['SecretAwsArgs']] = None,
             azure_connector: Optional[pulumi.Input['SecretAzureConnectorArgs']] = None,
             azure_sdk: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             dictionary: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             docker: Optional[pulumi.Input[str]] = None,
             ecr: Optional[pulumi.Input['SecretEcrArgs']] = None,
             gcp: Optional[pulumi.Input[str]] = None,
             keypair: Optional[pulumi.Input['SecretKeypairArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             nats_account: Optional[pulumi.Input['SecretNatsAccountArgs']] = None,
             opaque: Optional[pulumi.Input['SecretOpaqueArgs']] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             tls: Optional[pulumi.Input['SecretTlsArgs']] = None,
             userpass: Optional[pulumi.Input['SecretUserpassArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'azureConnector' in kwargs:
            azure_connector = kwargs['azureConnector']
        if 'azureSdk' in kwargs:
            azure_sdk = kwargs['azureSdk']
        if 'natsAccount' in kwargs:
            nats_account = kwargs['natsAccount']

        if aws is not None:
            _setter("aws", aws)
        if azure_connector is not None:
            _setter("azure_connector", azure_connector)
        if azure_sdk is not None:
            _setter("azure_sdk", azure_sdk)
        if description is not None:
            _setter("description", description)
        if dictionary is not None:
            _setter("dictionary", dictionary)
        if docker is not None:
            _setter("docker", docker)
        if ecr is not None:
            _setter("ecr", ecr)
        if gcp is not None:
            _setter("gcp", gcp)
        if keypair is not None:
            _setter("keypair", keypair)
        if name is not None:
            _setter("name", name)
        if nats_account is not None:
            _setter("nats_account", nats_account)
        if opaque is not None:
            _setter("opaque", opaque)
        if tags is not None:
            _setter("tags", tags)
        if tls is not None:
            _setter("tls", tls)
        if userpass is not None:
            _setter("userpass", userpass)

    @property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input['SecretAwsArgs']]:
        return pulumi.get(self, "aws")

    @aws.setter
    def aws(self, value: Optional[pulumi.Input['SecretAwsArgs']]):
        pulumi.set(self, "aws", value)

    @property
    @pulumi.getter(name="azureConnector")
    def azure_connector(self) -> Optional[pulumi.Input['SecretAzureConnectorArgs']]:
        return pulumi.get(self, "azure_connector")

    @azure_connector.setter
    def azure_connector(self, value: Optional[pulumi.Input['SecretAzureConnectorArgs']]):
        pulumi.set(self, "azure_connector", value)

    @property
    @pulumi.getter(name="azureSdk")
    def azure_sdk(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "azure_sdk")

    @azure_sdk.setter
    def azure_sdk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_sdk", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def dictionary(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "dictionary")

    @dictionary.setter
    def dictionary(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "dictionary", value)

    @property
    @pulumi.getter
    def docker(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "docker")

    @docker.setter
    def docker(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "docker", value)

    @property
    @pulumi.getter
    def ecr(self) -> Optional[pulumi.Input['SecretEcrArgs']]:
        return pulumi.get(self, "ecr")

    @ecr.setter
    def ecr(self, value: Optional[pulumi.Input['SecretEcrArgs']]):
        pulumi.set(self, "ecr", value)

    @property
    @pulumi.getter
    def gcp(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gcp")

    @gcp.setter
    def gcp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gcp", value)

    @property
    @pulumi.getter
    def keypair(self) -> Optional[pulumi.Input['SecretKeypairArgs']]:
        return pulumi.get(self, "keypair")

    @keypair.setter
    def keypair(self, value: Optional[pulumi.Input['SecretKeypairArgs']]):
        pulumi.set(self, "keypair", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="natsAccount")
    def nats_account(self) -> Optional[pulumi.Input['SecretNatsAccountArgs']]:
        return pulumi.get(self, "nats_account")

    @nats_account.setter
    def nats_account(self, value: Optional[pulumi.Input['SecretNatsAccountArgs']]):
        pulumi.set(self, "nats_account", value)

    @property
    @pulumi.getter
    def opaque(self) -> Optional[pulumi.Input['SecretOpaqueArgs']]:
        return pulumi.get(self, "opaque")

    @opaque.setter
    def opaque(self, value: Optional[pulumi.Input['SecretOpaqueArgs']]):
        pulumi.set(self, "opaque", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input['SecretTlsArgs']]:
        return pulumi.get(self, "tls")

    @tls.setter
    def tls(self, value: Optional[pulumi.Input['SecretTlsArgs']]):
        pulumi.set(self, "tls", value)

    @property
    @pulumi.getter
    def userpass(self) -> Optional[pulumi.Input['SecretUserpassArgs']]:
        return pulumi.get(self, "userpass")

    @userpass.setter
    def userpass(self, value: Optional[pulumi.Input['SecretUserpassArgs']]):
        pulumi.set(self, "userpass", value)


@pulumi.input_type
class _SecretState:
    def __init__(__self__, *,
                 aws: Optional[pulumi.Input['SecretAwsArgs']] = None,
                 azure_connector: Optional[pulumi.Input['SecretAzureConnectorArgs']] = None,
                 azure_sdk: Optional[pulumi.Input[str]] = None,
                 cpln_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dictionary: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 dictionary_as_envs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 docker: Optional[pulumi.Input[str]] = None,
                 ecr: Optional[pulumi.Input['SecretEcrArgs']] = None,
                 gcp: Optional[pulumi.Input[str]] = None,
                 keypair: Optional[pulumi.Input['SecretKeypairArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nats_account: Optional[pulumi.Input['SecretNatsAccountArgs']] = None,
                 opaque: Optional[pulumi.Input['SecretOpaqueArgs']] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tls: Optional[pulumi.Input['SecretTlsArgs']] = None,
                 userpass: Optional[pulumi.Input['SecretUserpassArgs']] = None):
        """
        Input properties used for looking up and filtering Secret resources.
        """
        _SecretState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            aws=aws,
            azure_connector=azure_connector,
            azure_sdk=azure_sdk,
            cpln_id=cpln_id,
            description=description,
            dictionary=dictionary,
            dictionary_as_envs=dictionary_as_envs,
            docker=docker,
            ecr=ecr,
            gcp=gcp,
            keypair=keypair,
            name=name,
            nats_account=nats_account,
            opaque=opaque,
            self_link=self_link,
            tags=tags,
            tls=tls,
            userpass=userpass,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             aws: Optional[pulumi.Input['SecretAwsArgs']] = None,
             azure_connector: Optional[pulumi.Input['SecretAzureConnectorArgs']] = None,
             azure_sdk: Optional[pulumi.Input[str]] = None,
             cpln_id: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             dictionary: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             dictionary_as_envs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             docker: Optional[pulumi.Input[str]] = None,
             ecr: Optional[pulumi.Input['SecretEcrArgs']] = None,
             gcp: Optional[pulumi.Input[str]] = None,
             keypair: Optional[pulumi.Input['SecretKeypairArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             nats_account: Optional[pulumi.Input['SecretNatsAccountArgs']] = None,
             opaque: Optional[pulumi.Input['SecretOpaqueArgs']] = None,
             self_link: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             tls: Optional[pulumi.Input['SecretTlsArgs']] = None,
             userpass: Optional[pulumi.Input['SecretUserpassArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'azureConnector' in kwargs:
            azure_connector = kwargs['azureConnector']
        if 'azureSdk' in kwargs:
            azure_sdk = kwargs['azureSdk']
        if 'cplnId' in kwargs:
            cpln_id = kwargs['cplnId']
        if 'dictionaryAsEnvs' in kwargs:
            dictionary_as_envs = kwargs['dictionaryAsEnvs']
        if 'natsAccount' in kwargs:
            nats_account = kwargs['natsAccount']
        if 'selfLink' in kwargs:
            self_link = kwargs['selfLink']

        if aws is not None:
            _setter("aws", aws)
        if azure_connector is not None:
            _setter("azure_connector", azure_connector)
        if azure_sdk is not None:
            _setter("azure_sdk", azure_sdk)
        if cpln_id is not None:
            _setter("cpln_id", cpln_id)
        if description is not None:
            _setter("description", description)
        if dictionary is not None:
            _setter("dictionary", dictionary)
        if dictionary_as_envs is not None:
            _setter("dictionary_as_envs", dictionary_as_envs)
        if docker is not None:
            _setter("docker", docker)
        if ecr is not None:
            _setter("ecr", ecr)
        if gcp is not None:
            _setter("gcp", gcp)
        if keypair is not None:
            _setter("keypair", keypair)
        if name is not None:
            _setter("name", name)
        if nats_account is not None:
            _setter("nats_account", nats_account)
        if opaque is not None:
            _setter("opaque", opaque)
        if self_link is not None:
            _setter("self_link", self_link)
        if tags is not None:
            _setter("tags", tags)
        if tls is not None:
            _setter("tls", tls)
        if userpass is not None:
            _setter("userpass", userpass)

    @property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input['SecretAwsArgs']]:
        return pulumi.get(self, "aws")

    @aws.setter
    def aws(self, value: Optional[pulumi.Input['SecretAwsArgs']]):
        pulumi.set(self, "aws", value)

    @property
    @pulumi.getter(name="azureConnector")
    def azure_connector(self) -> Optional[pulumi.Input['SecretAzureConnectorArgs']]:
        return pulumi.get(self, "azure_connector")

    @azure_connector.setter
    def azure_connector(self, value: Optional[pulumi.Input['SecretAzureConnectorArgs']]):
        pulumi.set(self, "azure_connector", value)

    @property
    @pulumi.getter(name="azureSdk")
    def azure_sdk(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "azure_sdk")

    @azure_sdk.setter
    def azure_sdk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_sdk", value)

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
    def dictionary(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "dictionary")

    @dictionary.setter
    def dictionary(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "dictionary", value)

    @property
    @pulumi.getter(name="dictionaryAsEnvs")
    def dictionary_as_envs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "dictionary_as_envs")

    @dictionary_as_envs.setter
    def dictionary_as_envs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "dictionary_as_envs", value)

    @property
    @pulumi.getter
    def docker(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "docker")

    @docker.setter
    def docker(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "docker", value)

    @property
    @pulumi.getter
    def ecr(self) -> Optional[pulumi.Input['SecretEcrArgs']]:
        return pulumi.get(self, "ecr")

    @ecr.setter
    def ecr(self, value: Optional[pulumi.Input['SecretEcrArgs']]):
        pulumi.set(self, "ecr", value)

    @property
    @pulumi.getter
    def gcp(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gcp")

    @gcp.setter
    def gcp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gcp", value)

    @property
    @pulumi.getter
    def keypair(self) -> Optional[pulumi.Input['SecretKeypairArgs']]:
        return pulumi.get(self, "keypair")

    @keypair.setter
    def keypair(self, value: Optional[pulumi.Input['SecretKeypairArgs']]):
        pulumi.set(self, "keypair", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="natsAccount")
    def nats_account(self) -> Optional[pulumi.Input['SecretNatsAccountArgs']]:
        return pulumi.get(self, "nats_account")

    @nats_account.setter
    def nats_account(self, value: Optional[pulumi.Input['SecretNatsAccountArgs']]):
        pulumi.set(self, "nats_account", value)

    @property
    @pulumi.getter
    def opaque(self) -> Optional[pulumi.Input['SecretOpaqueArgs']]:
        return pulumi.get(self, "opaque")

    @opaque.setter
    def opaque(self, value: Optional[pulumi.Input['SecretOpaqueArgs']]):
        pulumi.set(self, "opaque", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input['SecretTlsArgs']]:
        return pulumi.get(self, "tls")

    @tls.setter
    def tls(self, value: Optional[pulumi.Input['SecretTlsArgs']]):
        pulumi.set(self, "tls", value)

    @property
    @pulumi.getter
    def userpass(self) -> Optional[pulumi.Input['SecretUserpassArgs']]:
        return pulumi.get(self, "userpass")

    @userpass.setter
    def userpass(self, value: Optional[pulumi.Input['SecretUserpassArgs']]):
        pulumi.set(self, "userpass", value)


class Secret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws: Optional[pulumi.Input[pulumi.InputType['SecretAwsArgs']]] = None,
                 azure_connector: Optional[pulumi.Input[pulumi.InputType['SecretAzureConnectorArgs']]] = None,
                 azure_sdk: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dictionary: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 docker: Optional[pulumi.Input[str]] = None,
                 ecr: Optional[pulumi.Input[pulumi.InputType['SecretEcrArgs']]] = None,
                 gcp: Optional[pulumi.Input[str]] = None,
                 keypair: Optional[pulumi.Input[pulumi.InputType['SecretKeypairArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nats_account: Optional[pulumi.Input[pulumi.InputType['SecretNatsAccountArgs']]] = None,
                 opaque: Optional[pulumi.Input[pulumi.InputType['SecretOpaqueArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tls: Optional[pulumi.Input[pulumi.InputType['SecretTlsArgs']]] = None,
                 userpass: Optional[pulumi.Input[pulumi.InputType['SecretUserpassArgs']]] = None,
                 __props__=None):
        """
        Create a Secret resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SecretArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Secret resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SecretArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws: Optional[pulumi.Input[pulumi.InputType['SecretAwsArgs']]] = None,
                 azure_connector: Optional[pulumi.Input[pulumi.InputType['SecretAzureConnectorArgs']]] = None,
                 azure_sdk: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dictionary: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 docker: Optional[pulumi.Input[str]] = None,
                 ecr: Optional[pulumi.Input[pulumi.InputType['SecretEcrArgs']]] = None,
                 gcp: Optional[pulumi.Input[str]] = None,
                 keypair: Optional[pulumi.Input[pulumi.InputType['SecretKeypairArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nats_account: Optional[pulumi.Input[pulumi.InputType['SecretNatsAccountArgs']]] = None,
                 opaque: Optional[pulumi.Input[pulumi.InputType['SecretOpaqueArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tls: Optional[pulumi.Input[pulumi.InputType['SecretTlsArgs']]] = None,
                 userpass: Optional[pulumi.Input[pulumi.InputType['SecretUserpassArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecretArgs.__new__(SecretArgs)

            if aws is not None and not isinstance(aws, SecretAwsArgs):
                aws = aws or {}
                def _setter(key, value):
                    aws[key] = value
                SecretAwsArgs._configure(_setter, **aws)
            __props__.__dict__["aws"] = aws
            if azure_connector is not None and not isinstance(azure_connector, SecretAzureConnectorArgs):
                azure_connector = azure_connector or {}
                def _setter(key, value):
                    azure_connector[key] = value
                SecretAzureConnectorArgs._configure(_setter, **azure_connector)
            __props__.__dict__["azure_connector"] = azure_connector
            __props__.__dict__["azure_sdk"] = None if azure_sdk is None else pulumi.Output.secret(azure_sdk)
            __props__.__dict__["description"] = description
            __props__.__dict__["dictionary"] = dictionary
            __props__.__dict__["docker"] = None if docker is None else pulumi.Output.secret(docker)
            if ecr is not None and not isinstance(ecr, SecretEcrArgs):
                ecr = ecr or {}
                def _setter(key, value):
                    ecr[key] = value
                SecretEcrArgs._configure(_setter, **ecr)
            __props__.__dict__["ecr"] = ecr
            __props__.__dict__["gcp"] = None if gcp is None else pulumi.Output.secret(gcp)
            if keypair is not None and not isinstance(keypair, SecretKeypairArgs):
                keypair = keypair or {}
                def _setter(key, value):
                    keypair[key] = value
                SecretKeypairArgs._configure(_setter, **keypair)
            __props__.__dict__["keypair"] = keypair
            __props__.__dict__["name"] = name
            if nats_account is not None and not isinstance(nats_account, SecretNatsAccountArgs):
                nats_account = nats_account or {}
                def _setter(key, value):
                    nats_account[key] = value
                SecretNatsAccountArgs._configure(_setter, **nats_account)
            __props__.__dict__["nats_account"] = nats_account
            if opaque is not None and not isinstance(opaque, SecretOpaqueArgs):
                opaque = opaque or {}
                def _setter(key, value):
                    opaque[key] = value
                SecretOpaqueArgs._configure(_setter, **opaque)
            __props__.__dict__["opaque"] = opaque
            __props__.__dict__["tags"] = tags
            if tls is not None and not isinstance(tls, SecretTlsArgs):
                tls = tls or {}
                def _setter(key, value):
                    tls[key] = value
                SecretTlsArgs._configure(_setter, **tls)
            __props__.__dict__["tls"] = tls
            if userpass is not None and not isinstance(userpass, SecretUserpassArgs):
                userpass = userpass or {}
                def _setter(key, value):
                    userpass[key] = value
                SecretUserpassArgs._configure(_setter, **userpass)
            __props__.__dict__["userpass"] = userpass
            __props__.__dict__["cpln_id"] = None
            __props__.__dict__["dictionary_as_envs"] = None
            __props__.__dict__["self_link"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["azureSdk", "docker", "gcp"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Secret, __self__).__init__(
            'cpln:index/secret:Secret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aws: Optional[pulumi.Input[pulumi.InputType['SecretAwsArgs']]] = None,
            azure_connector: Optional[pulumi.Input[pulumi.InputType['SecretAzureConnectorArgs']]] = None,
            azure_sdk: Optional[pulumi.Input[str]] = None,
            cpln_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dictionary: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            dictionary_as_envs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            docker: Optional[pulumi.Input[str]] = None,
            ecr: Optional[pulumi.Input[pulumi.InputType['SecretEcrArgs']]] = None,
            gcp: Optional[pulumi.Input[str]] = None,
            keypair: Optional[pulumi.Input[pulumi.InputType['SecretKeypairArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nats_account: Optional[pulumi.Input[pulumi.InputType['SecretNatsAccountArgs']]] = None,
            opaque: Optional[pulumi.Input[pulumi.InputType['SecretOpaqueArgs']]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tls: Optional[pulumi.Input[pulumi.InputType['SecretTlsArgs']]] = None,
            userpass: Optional[pulumi.Input[pulumi.InputType['SecretUserpassArgs']]] = None) -> 'Secret':
        """
        Get an existing Secret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretState.__new__(_SecretState)

        __props__.__dict__["aws"] = aws
        __props__.__dict__["azure_connector"] = azure_connector
        __props__.__dict__["azure_sdk"] = azure_sdk
        __props__.__dict__["cpln_id"] = cpln_id
        __props__.__dict__["description"] = description
        __props__.__dict__["dictionary"] = dictionary
        __props__.__dict__["dictionary_as_envs"] = dictionary_as_envs
        __props__.__dict__["docker"] = docker
        __props__.__dict__["ecr"] = ecr
        __props__.__dict__["gcp"] = gcp
        __props__.__dict__["keypair"] = keypair
        __props__.__dict__["name"] = name
        __props__.__dict__["nats_account"] = nats_account
        __props__.__dict__["opaque"] = opaque
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tls"] = tls
        __props__.__dict__["userpass"] = userpass
        return Secret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def aws(self) -> pulumi.Output[Optional['outputs.SecretAws']]:
        return pulumi.get(self, "aws")

    @property
    @pulumi.getter(name="azureConnector")
    def azure_connector(self) -> pulumi.Output[Optional['outputs.SecretAzureConnector']]:
        return pulumi.get(self, "azure_connector")

    @property
    @pulumi.getter(name="azureSdk")
    def azure_sdk(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "azure_sdk")

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
    def dictionary(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "dictionary")

    @property
    @pulumi.getter(name="dictionaryAsEnvs")
    def dictionary_as_envs(self) -> pulumi.Output[Mapping[str, Any]]:
        return pulumi.get(self, "dictionary_as_envs")

    @property
    @pulumi.getter
    def docker(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "docker")

    @property
    @pulumi.getter
    def ecr(self) -> pulumi.Output[Optional['outputs.SecretEcr']]:
        return pulumi.get(self, "ecr")

    @property
    @pulumi.getter
    def gcp(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "gcp")

    @property
    @pulumi.getter
    def keypair(self) -> pulumi.Output[Optional['outputs.SecretKeypair']]:
        return pulumi.get(self, "keypair")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natsAccount")
    def nats_account(self) -> pulumi.Output[Optional['outputs.SecretNatsAccount']]:
        return pulumi.get(self, "nats_account")

    @property
    @pulumi.getter
    def opaque(self) -> pulumi.Output[Optional['outputs.SecretOpaque']]:
        return pulumi.get(self, "opaque")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tls(self) -> pulumi.Output[Optional['outputs.SecretTls']]:
        return pulumi.get(self, "tls")

    @property
    @pulumi.getter
    def userpass(self) -> pulumi.Output[Optional['outputs.SecretUserpass']]:
        return pulumi.get(self, "userpass")
