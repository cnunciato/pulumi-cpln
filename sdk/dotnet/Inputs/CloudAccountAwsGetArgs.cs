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

    public sealed class CloudAccountAwsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        public CloudAccountAwsGetArgs()
        {
        }
        public static new CloudAccountAwsGetArgs Empty => new CloudAccountAwsGetArgs();
    }
}
