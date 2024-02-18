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
    public sealed class GvcControlplaneTracing
    {
        public readonly ImmutableDictionary<string, string>? CustomTags;
        public readonly int Sampling;

        [OutputConstructor]
        private GvcControlplaneTracing(
            ImmutableDictionary<string, string>? customTags,

            int sampling)
        {
            CustomTags = customTags;
            Sampling = sampling;
        }
    }
}
