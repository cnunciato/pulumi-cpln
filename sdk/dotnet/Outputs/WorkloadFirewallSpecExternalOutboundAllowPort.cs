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
    public sealed class WorkloadFirewallSpecExternalOutboundAllowPort
    {
        public readonly int Number;
        public readonly string Protocol;

        [OutputConstructor]
        private WorkloadFirewallSpecExternalOutboundAllowPort(
            int number,

            string protocol)
        {
            Number = number;
            Protocol = protocol;
        }
    }
}
