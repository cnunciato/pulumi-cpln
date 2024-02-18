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
    public sealed class WorkloadFirewallSpec
    {
        public readonly Outputs.WorkloadFirewallSpecExternal? External;
        public readonly Outputs.WorkloadFirewallSpecInternal? Internal;

        [OutputConstructor]
        private WorkloadFirewallSpec(
            Outputs.WorkloadFirewallSpecExternal? external,

            Outputs.WorkloadFirewallSpecInternal? @internal)
        {
            External = external;
            Internal = @internal;
        }
    }
}