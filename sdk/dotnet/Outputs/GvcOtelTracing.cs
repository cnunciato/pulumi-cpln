// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Outputs
{

    [OutputType]
    public sealed class GvcOtelTracing
    {
        public readonly ImmutableDictionary<string, string>? CustomTags;
        public readonly string Endpoint;
        public readonly int Sampling;

        [OutputConstructor]
        private GvcOtelTracing(
            ImmutableDictionary<string, string>? customTags,

            string endpoint,

            int sampling)
        {
            CustomTags = customTags;
            Endpoint = endpoint;
            Sampling = sampling;
        }
    }
}