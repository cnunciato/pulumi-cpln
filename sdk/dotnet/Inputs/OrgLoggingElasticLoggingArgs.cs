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

    public sealed class OrgLoggingElasticLoggingArgs : global::Pulumi.ResourceArgs
    {
        [Input("aws")]
        public Input<Inputs.OrgLoggingElasticLoggingAwsArgs>? Aws { get; set; }

        [Input("elasticCloud")]
        public Input<Inputs.OrgLoggingElasticLoggingElasticCloudArgs>? ElasticCloud { get; set; }

        [Input("generic")]
        public Input<Inputs.OrgLoggingElasticLoggingGenericArgs>? Generic { get; set; }

        public OrgLoggingElasticLoggingArgs()
        {
        }
        public static new OrgLoggingElasticLoggingArgs Empty => new OrgLoggingElasticLoggingArgs();
    }
}
