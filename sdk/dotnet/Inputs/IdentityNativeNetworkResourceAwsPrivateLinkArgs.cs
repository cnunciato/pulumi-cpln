// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Inputs
{

    public sealed class IdentityNativeNetworkResourceAwsPrivateLinkArgs : global::Pulumi.ResourceArgs
    {
        [Input("endpointServiceName", required: true)]
        public Input<string> EndpointServiceName { get; set; } = null!;

        public IdentityNativeNetworkResourceAwsPrivateLinkArgs()
        {
        }
        public static new IdentityNativeNetworkResourceAwsPrivateLinkArgs Empty => new IdentityNativeNetworkResourceAwsPrivateLinkArgs();
    }
}
