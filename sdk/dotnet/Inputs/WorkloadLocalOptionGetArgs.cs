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

    public sealed class WorkloadLocalOptionGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("autoscaling", required: true)]
        public Input<Inputs.WorkloadLocalOptionAutoscalingGetArgs> Autoscaling { get; set; } = null!;

        [Input("capacityAi")]
        public Input<bool>? CapacityAi { get; set; }

        [Input("debug")]
        public Input<bool>? Debug { get; set; }

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("suspend")]
        public Input<bool>? Suspend { get; set; }

        [Input("timeoutSeconds")]
        public Input<int>? TimeoutSeconds { get; set; }

        public WorkloadLocalOptionGetArgs()
        {
        }
        public static new WorkloadLocalOptionGetArgs Empty => new WorkloadLocalOptionGetArgs();
    }
}